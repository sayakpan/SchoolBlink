//SUBMISSION TOAST


function submitForm(event, formid) {
    // Prevent form submission
    event.preventDefault();

    $(document).ready(function () {
        $('.toast').toast('show');
    });

    // submit the form programmatically after executing JavaScript
    setTimeout(function () {
        // Submit the form programmatically
        document.getElementById(formid).submit();
        is_successfull = true
    }, 1000);
}


// SAVE BUTTON LOADING SPINNER

function saving(button) {
    button.textContent = "Saving";
    button.innerHTML += "<span class='ms-2 spinner-border spinner-border-sm' role='status' aria-hidden='true'></span>";
}

var saveButton = document.getElementById("SaveBtn");
saveButton.addEventListener("click", function () {
    saving(saveButton);
});

var PersonalSaveBtn = document.getElementById("PersonalSaveBtn");
PersonalSaveBtn.addEventListener("click", function () {
    saving(PersonalSaveBtn);
});


// function saving() {
//     var button = this;
//     button.textContent = "Saving";
//     button.innerHTML += "<span class='ms-2 spinner-border spinner-border-sm' role='status' aria-hidden='true'></span>";
// }

// document.getElementById("SaveBtn").addEventListener('click', saving)
// document.getElementById("PersonalSaveBtn").addEventListener('click', saving)

// DATE OF BIRTH CUSTOM VALIDITY CHECK

document.getElementById("dateOfBirthInput").addEventListener("input", function () {
    var dateOfBirthInput = this;
    var dateOfBirthInputValue = this.value;
    var validFormat = /^(\d{1,2}) ([a-zA-Z]{3}) (\d{4})$/;

    if (!validFormat.test(dateOfBirthInputValue)) {
        previousBorderColor = dateOfBirthInput.style.borderColor;
        dateOfBirthInput.style.borderColor = 'red';
        this.setCustomValidity("Please enter the date in the format 'DD MMM YYYY'");
    } else {
        dateOfBirthInput.style.borderColor = previousBorderColor
        this.setCustomValidity("");
    }
});

// DATE PICKER

$(document).ready(function () {
    $("#dateOfBirthInput").datepicker({
        dateFormat: 'd M yy',
        // Additional configuration options for the datepicker can be added here
    });
});

$(document).ready(function () {
    $("#ChilddateOfBirthInput").datepicker({
        dateFormat: 'd M yy',
        // Additional configuration options for the datepicker can be added here
    });
});

// RESET PASSWORD CONFIRMATION

const oldPassword = document.getElementById("oldPassword");
const newPassword = document.getElementById("newPassword");
const confirmPassword = document.getElementById("confirmPassword");
const resetBtn = document.getElementById("resetBtn");

resetBtn.disabled = true

function validatePasswords() {
    const newPwd = newPassword.value.trim();
    const confirmPwd = confirmPassword.value.trim();

    if (newPwd === "" || confirmPwd === "") {
        newPassword.style.borderColor = "";
        confirmPassword.style.borderColor = "";
        resetBtn.disabled = true
    } else if (newPwd.length < 6 && confirmPwd.length < 6) {
        confirmPassword.style.borderColor = "red";
        newPassword.style.borderColor = "red";
        resetBtn.disabled = true
    }
    else if (newPwd !== confirmPwd) {
        confirmPassword.style.borderColor = "red";
        newPassword.style.borderColor = "red";
        resetBtn.disabled = true
    } else {
        confirmPassword.style.borderColor = "green";
        newPassword.style.borderColor = "green";
        resetBtn.disabled = false
    }

}

newPassword.addEventListener("input", validatePasswords)
confirmPassword.addEventListener("input", validatePasswords)


// MODAL for EACH CHILD

var modal = document.getElementById('updateChildModal');

const child_name = document.getElementById('childname');
const dob = document.getElementById('child_date_of_birth')
const childgender1 = document.getElementById('childgender1')
const childgender2 = document.getElementById('childgender2')
const interested_class = document.getElementById('interested_class_update')
const childid = document.getElementById('childidhidden')

modal.addEventListener('show.bs.modal', function (event) {
    var button = event.relatedTarget;
    var childID = button.getAttribute('data-child-id');
    var childName = button.parentNode.querySelector('.card-title').innerText;
    var DOB = button.parentNode.querySelector('#addedchilddob').innerText;
    var Gender = button.parentNode.querySelector('#addedchildgender').innerText;
    var ChildClass = button.parentNode.querySelector('#addedchildclass').innerText;

    childid.value = childID
    child_name.value = childName;
    dob.value = DOB;

    for (let i = 0; i < interested_class.options.length; i++) {
        const option = interested_class.options[i];
        if (option.text === ChildClass) {
            option.selected = true;
            break;
        }
    }

    if (Gender === 'Boy') {
        childgender1.checked = true
    }
    else {
        childgender2.checked = true
    }
});

// Delete Modal

const deleteButtons = document.querySelectorAll('.btn-outline-danger[data-bs-toggle="modal"][data-bs-target="#deleteChildModal"]');
const childIdInput = document.getElementById('child_id_delete');
const deleteChildForm = document.getElementById('deleteChildForm');

deleteButtons.forEach(button => {
    button.addEventListener('click', function () {
        const childId = this.dataset.childId;
        childIdInput.value = childId;
        deleteChildForm.action = "{% url 'Parent:deletechild' pk=" + childId + " %}";
    });
});


