// Profile DropDown Menu


const profile = document.querySelector('.profile');
const dropdown = document.querySelector('.dropdown__wrapper');

profile.addEventListener('click', () => {
    dropdown.classList.remove('none');
    dropdown.classList.toggle('hide');
})


document.addEventListener("click", (event) => {
    const isClickInsideDropdown = dropdown.contains(event.target);
    const isProfileClicked = profile.contains(event.target);

    if (!isClickInsideDropdown && !isProfileClicked) {
        dropdown.classList.add('hide');
        dropdown.classList.add('dropdown__wrapper--fade-in');
    }
});

// BootStrap Tooltip Script

const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

// Bootstrap Toast 

const option = {
    animation: true,
    autohide: true,
    delay: 5000
};
const toastElList = document.querySelectorAll('.toast')
const toastList = [...toastElList].map(toastEl => new bootstrap.Toast(toastEl, option))

// Sign Up PassWord Confirmation

const first_name = document.getElementById("fname")
const email = document.getElementById("emailid")
const password1 = document.getElementById("pass1")
const password2 = document.getElementById("pass2")
const signupButton = document.getElementById("signupbtn")
var errorSpan = document.getElementById("passwordError");

signupButton.disabled = true;

function toggleStyle() {
    if (password1.value.trim() !== "" && password2.value.trim() !== "") {
        if (password1.value.length < 6) {
            signupButton.disabled = true;
            password1.style.borderColor = 'red';
            password2.style.borderColor = 'red';
            errorSpan.textContent = "Passwords too short";
            errorSpan.style.color = "red";
        }
        else if (password1.value !== password2.value) {
            signupButton.disabled = true;
            password1.style.borderColor = 'red';
            password2.style.borderColor = 'red';
            errorSpan.textContent = "Passwords do not match";
            errorSpan.style.color = "red";
        } else {
            signupButton.disabled = false;
            password1.style.borderWidth = '2px';
            password2.style.borderWidth = '2px';
            password1.style.borderColor = 'lightgreen';
            password2.style.borderColor = 'lightgreen';
            errorSpan.textContent = "";
        }
    }
    else {
        signupButton.disabled = true;
    }
}

function checkEmptyField(element) {
    if (element.value.trim() !== "") {
        element.style.borderColor = "lightgreen";
        element.style.borderWidth = '2px';
    } else {
        element.style.borderColor = "red";
    }
}


first_name.addEventListener("input", function () {
    checkEmptyField(first_name);
});

email.addEventListener("input", function () {
    checkEmptyField(email);
});


password1.addEventListener('input', toggleStyle);
password2.addEventListener('input', toggleStyle);