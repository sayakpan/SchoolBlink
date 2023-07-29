import razorpay
from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.urls import reverse
from django.conf import settings

from Accounts.models import User
from Parent.models import *
from Profiles.models import *
from Admissions.models import *

from Parent.forms import *
from Admissions.forms import *


class ParentTest(UserPassesTestMixin):
    def test_func(self) -> bool | None:
        return self.request.user.is_parent


# Create your views here.


class SchoolApplicationView(TemplateView, LoginRequiredMixin, ParentTest):
    model = ApplicationForm
    template_name = "Admissions/application.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        slug = self.kwargs.get("slug")
        class_id = self.kwargs.get("class_id")
        school = School_Profiles.objects.get(slug=slug)
        parent = ParentProfile.objects.get(user=user)
        class_applied_for = AdmissionOpenClasses.objects.get(
            school=school, class_opened=class_id
        )
        context["parent"] = parent
        context["school"] = school
        context["class_applied_for"] = class_applied_for
        return context


class SchoolApplicationSubmitView(CreateView, LoginRequiredMixin, ParentTest):
    model = ApplicationForm
    form_class = SchoolApplicationForm
    template_name = "Admissions/application.html"

    def get_success_url(self) -> str:
        pk = self.object.pk
        return reverse("Admissions:checkout", kwargs={"pk": pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        slug = self.kwargs.get("slug")
        class_id = self.kwargs.get("class_id")
        school = School_Profiles.objects.get(slug=slug)
        parent = ParentProfile.objects.get(user=user)
        class_applied_for = AdmissionOpenClasses.objects.get(
            school=school, class_opened=class_id
        )
        context["parent"] = parent
        context["school"] = school
        context["class_applied_for"] = class_applied_for
        return context

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        print(form.cleaned_data)
        print(form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        parent_id = form.cleaned_data.get("parent")
        school_id = form.cleaned_data.get("school")
        child = form.cleaned_data.get("child")
        submitted_for_class = form.cleaned_data.get("submitted_for_class")

        application = form.instance
        application.parent = parent_id
        application.school = school_id
        application.submitted_for_class = submitted_for_class
        application.child = child
        application.name = child.name
        application.gender = child.gender
        application.date_of_birth = child.date_of_birth
        application.blood_group = form.cleaned_data.get("blood_group")
        application.mother_toungh = form.cleaned_data.get("mother_toungh")
        application.religion = form.cleaned_data.get("religion")
        application.category = form.cleaned_data.get("category")
        application.address = form.cleaned_data.get("address")
        application.save()
        print("SchoolApplicationSubmitView : Application Submitted")
        return super().form_valid(form)


razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET)
)


class SchoolApplicationPaymentView(TemplateView, LoginRequiredMixin, ParentTest):
    template_name = "Admissions/checkout.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        razorpay_client = razorpay.Client(
            auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET)
        )
        context = super().get_context_data(**kwargs)
        application = ApplicationForm.objects.get(id=self.kwargs.get("pk"))

        amount = application.submitted_for_class.form_price
        amount = amount * 100  # Converted to Razorpay Paise
        currency = "INR"

        razorpay_order = razorpay_client.order.create(
            dict(amount=amount, currency=currency, payment_capture="0")
        )
        razorpay_order_id = razorpay_order["id"]
        callback_url = "paymenthandler/"
        # we need to pass these details to frontend.
        context = {}
        context["application"] = application
        context["razorpay_order_id"] = razorpay_order_id
        context["razorpay_merchant_key"] = settings.RAZOR_KEY_ID
        context["razorpay_amount"] = amount
        context["currency"] = currency
        context["callback_url"] = callback_url
        context["application"] = application
        return context


@csrf_exempt
def paymenthandler(request, pk):
    application = ApplicationForm.objects.get(id=pk)
    amount = application.submitted_for_class.form_price
    amount = amount * 100
    if request.method == "POST":
        payment_id = request.POST.get("razorpay_payment_id")
        razorpay_order_id = request.POST.get("razorpay_order_id")
        signature = request.POST.get("razorpay_signature")

        params_dict = {
            "razorpay_order_id": razorpay_order_id,
            "razorpay_payment_id": payment_id,
            "razorpay_signature": signature,
        }

        result = razorpay_client.utility.verify_payment_signature(params_dict)

        if result is not None:
            try:
                razorpay_client.payment.capture(payment_id, amount)
                application.is_paid = True
                application.save()
                return render(request, "Admissions/paymentsuccess.html")
            except:
                return render(request, "Admissions/paymentfail.html")
        else:
            return render(request, "Admissions/paymentfail.html")
    else:
        print("other than POST request is made.")
        return HttpResponseBadRequest()
