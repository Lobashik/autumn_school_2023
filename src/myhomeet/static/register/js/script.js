const newPhotoContainer = document.getElementById('photo_ava_container');
const imgElement = document.createElement('img');
const cross = document.createElement('img');
const removedElements = [];
const fileInput = document.getElementById('input_file');
const imageContainer = document.getElementById('image_container');
let correctNumberFlug = false;
let correctTgFlug = false;
let img;

function uploadAva() {
    fileInput.addEventListener('change', function (e) {
        const selectedFile = e.target.files[0];
        const reader = new FileReader();
        reader.onload = function (event) {
            img = selectedFile;
            imgElement.src = event.target.result;
            imgElement.style.width = "100%";
            imgElement.style.height = "100%";
            imgElement.style.objectFit = "cover";
            imgElement.style.borderRadius = "16px";
            imageContainer.classList.toggle('new_your_page__image')
            imageContainer.appendChild(imgElement);
            const secondImgElement = imgElement.cloneNode(0);
            newPhotoContainer.classList.toggle('new_photo_ava_container');
            while (newPhotoContainer.firstChild) {
                const removedElement = newPhotoContainer.removeChild(newPhotoContainer.firstChild);
                removedElements.push(removedElement);
            };
            newPhotoContainer.appendChild(secondImgElement);
            const crossContainer = document.createElement('div');
            crossContainer.classList.add('new_photo_ava_container__cross_container');
            newPhotoContainer.appendChild(crossContainer);
            cross.classList.add('new_photo_ava_container__cross');
            cross.src = '/static/register/img/cross.svg'
            crossContainer.appendChild(cross);
        };
        reader.readAsDataURL(selectedFile);
    });
};

function closePhoto() {
    cross.addEventListener('click', function() {
        newPhotoContainer.classList.toggle('new_photo_ava_container');
        imageContainer.classList.toggle('new_your_page__image')
        imageContainer.removeChild(imgElement)
        while (newPhotoContainer.firstChild) {
            newPhotoContainer.removeChild(newPhotoContainer.firstChild);
        };
        for (const removedElement of removedElements) {
            newPhotoContainer.appendChild(removedElement);
        };
        fileInput.value = ''
    });
};

function sex() {
    const radioButtons = document.querySelectorAll('input[type="radio"][name="sex"]');
    const resultDiv = document.getElementById('sex');
    radioButtons.forEach(radio => {
        radio.addEventListener('change', function() {
            if (radio.checked) {
                if (radio.value == "F") {
                    correctValue = "Девушка"
                }
                else if (radio.value == "M") {
                    correctValue = "Парень"
                }
                resultDiv.textContent = correctValue;
            }
        });
    });
};

function correctNumber() {
    let inputNumberElement = document.getElementById('input_number');
    let labelNumberElement = document.getElementById('input_number_label');
    let parentDiv = inputNumberElement.parentElement;
    inputNumberElement.addEventListener('input', function() {
        let number = inputNumberElement.value;
        if ((number[0] === '7' && number.length === 11) || (number[0] === '8' && number.length === 11)) {
            inputNumberElement.style.background = "#F4F4F6";
            inputNumberElement.style.border = "1px solid #F4F4F6";
            parentDiv.classList.remove('name');
            labelNumberElement.setAttribute('style', 'display: None');
            correctNumberFlug = true;
        }
        else {
            parentDiv.classList.add('name');
            inputNumberElement.style.background = "rgba(255, 0, 0, 0.05)";
            inputNumberElement.style.border = "1px solid #ff0000";
            labelNumberElement.removeAttribute("style");
            correctNumberFlug = false;
        };
    });
};

function correctTg() {
    let inputNumberElement = document.getElementById('input_tg');
    let labelNumberElement = document.getElementById('input_tg_label');
    let textElementLenght = document.getElementById('length');
    let textElementDog = document.getElementById('dog');
    let parentDiv = inputNumberElement.parentElement;
    inputNumberElement.addEventListener('input', function() {
        let tg = inputNumberElement.value;
        if (tg[0] === '@' && tg.length >= 6) {
            inputNumberElement.style.background = "#F4F4F6";
            inputNumberElement.style.border = "1px solid #F4F4F6";
            parentDiv.classList.remove('name');
            labelNumberElement.setAttribute('style', 'display: None');
            correctTgFlug = true;
        }
        else if (tg[0] != '@') {
            parentDiv.classList.add('name');
            inputNumberElement.style.background = "rgba(255, 0, 0, 0.05)";
            inputNumberElement.style.border = "1px solid #ff0000";
            inputNumberElement.style.border = "1px solid #ff0000";
            labelNumberElement.removeAttribute("style");
            textElementDog.removeAttribute('style');
            textElementLenght.setAttribute('style', 'display: None');
            correctTgFlug = false;
        }
        else {
            parentDiv.classList.add('name');
            inputNumberElement.style.background = "rgba(255, 0, 0, 0.05)";
            inputNumberElement.style.border = "1px solid #ff0000";
            labelNumberElement.removeAttribute("style");
            textElementLenght.removeAttribute('style');
            textElementDog.setAttribute('style', 'display: None');
            correctTgFlug = false;
        };
    });
};

function textToP() {
    const textarea = document.getElementById("aboutme");
    const displayText = document.getElementById("display_text");
    textarea.addEventListener("input", function() {
        const userInput = textarea.value;
        displayText.textContent = userInput;
        if (userInput) {
            displayText.style.background = "none";
          } 
        else {
            displayText.style.background = "#EEEEF1";
          };
    });
}

function nameTop() {
    const nameText = document.getElementById("name")
    const displayName = document.getElementById("display_name")
    nameText.addEventListener("input", function() {
        const nameInput = nameText.value;
        if (nameInput) {
            displayName.textContent = nameInput;;
        }
        else {
            displayName.textContent = "Ваше имя";
        }
    })
}

function buttonContinue() {
    let inputFile = document.getElementById('input_file');
    let name = document.getElementById('name');
    let data = document.getElementById('data');
    let inputNumber = document.getElementById('input_number');
    let inputTg = document.getElementById('input_tg');
    let aboutme = document.getElementById('aboutme');
    let fields = [inputFile, name, data, inputNumber, inputTg, aboutme];
    let isValid = true;
    let count = -1;
    let countError = 0;
    document.getElementById('continue').addEventListener('click', function(event) {
        event.preventDefault();
        errorContinue();});
    document.getElementById('continue').addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            errorContinue();
        }
    });    
    function errorContinue() {
        for (let i = 0; i < fields.length; i++) {
            if (fields[i].value === '' && count === -1) {
                countError += 1;
                fields[i].style.background = 'rgba(255, 0, 0, 0.05)';
                fields[i].style.border = '1px solid #ff0000';
                let errorLabel = document.createElement('label');
                let errorParagraph = document.createElement('p');
                errorParagraph.textContent = 'Это обязательное поле';
                errorParagraph.classList.add('text', 'name_text', 'err');
                errorParagraph.style.textAlign = 'right';
                errorLabel.appendChild(errorParagraph);
                fields[i].insertAdjacentElement('afterend', errorLabel);
                if (i >= 1) {
                    fields[i].parentElement.classList.add('name');
                }                
                isValid = false;
            } 
            else {
                for (let i = 0; i < fields.length; i++) {
                    fields[i].addEventListener('input', function () {
                        fields[i].style.borderColor = '';
                        fields[i].style.background = '';
                        fields[i].style.border = '';
                        let errorLabel = fields[i].nextElementSibling;
                        if (errorLabel && errorLabel.tagName === "LABEL") {
                            errorLabel.remove();
                            countError -= 1};
                    });
                };
            };
        };
        if (countError === 0 && correctNumberFlug === true && correctTgFlug === true) {
            isValid = true;
        }
        else {
            count = 0;
        }
        if (isValid) {
            document.getElementById("page1").style.display = "None";
            document.getElementById("page2").style.display = "block";
            document.getElementById("flex_page2").style.display = "flex";
            document.getElementById("flex_page1").style.display = "None";
            document.getElementById("die_student").style.display = "block";
            document.getElementById("die_page1").style.display = "None";
            document.getElementById("register").style.display = "inline-block";
            document.getElementById("continue").style.display = "None";
            window.scrollTo(0, 0)
        };
    };   
};

function employeeOrStudent() {
    let employee = document.getElementById('employee_colomn');
    let student = document.getElementById('student_colomn');
    let radioEmployee = document.getElementById('employee');
    let radioStudent = document.getElementById('student');
    let dieEmployee = document.getElementById('die_employee');
    let dieStudent = document.getElementById('die_student');
    radioEmployee.addEventListener('change', function() {
        employee.style.display = 'flex';
        student.style.display = 'None';
        dieEmployee.style.display = "block";
        dieStudent.style.display = 'None';
    });
    radioStudent.addEventListener('change', function() {
        employee.style.display = 'None';
        student.style.display = 'flex';
        dieEmployee.style.display = "None";
        dieStudent.style.display = 'block';
    })
};

function textWork() {
    const textarea = document.getElementById("work");
    const displayText = document.getElementById("work_display_text");
    textarea.addEventListener("input", function() {
        const userInput = textarea.value;
        displayText.textContent = userInput;
        if (userInput) {
            displayText.style.background = "none";
          } 
        else {
            displayText.style.background = "#EEEEF1";
          };
    });
}

function textWorkStudent() {
    const textarea = document.getElementById("work_student");
    const displayText = document.getElementById("work_display_text");
    textarea.addEventListener("input", function() {
        const userInput = textarea.value;
        displayText.textContent = userInput;
        if (userInput) {
            displayText.style.background = "none";
          } 
        else {
            displayText.style.background = "#EEEEF1";
          };
    });
};

function grade() {
    document.addEventListener("DOMContentLoaded", function () {
        const gradeLabels = document.querySelectorAll(".grade_education");
        const endCheckbox = document.getElementById("end");
        const result = document.getElementById("grade_text");

        gradeLabels.forEach(function (label) {
            label.addEventListener("click", function () {
                gradeLabels.forEach(function (label) {
                    label.classList.remove("selected");
                });
                label.classList.add("selected");
                endCheckbox.checked = false;
                const selectedValue = label.querySelector("input").value;
                if (selectedValue) {
                    result.style.background = "none";
                    } 
                else {
                    result.style.background = "#EEEEF1";
                    };
                result.textContent = selectedValue + " курс";
            });
        });

        endCheckbox.addEventListener("change", function () {
            gradeLabels.forEach(function (label) {
                label.classList.remove("selected");
            });
            result.textContent = "Уже окончил";
            result.style.background = "none";
        });
    });    
};

function selectLevelEducation() {
    const select = document.getElementById("level_education");
    const div = document.getElementById("grade_text_1");
    const circle = document.getElementById("grade_text_1__circle")
    select.addEventListener('change', function() {
        const selectOption = select.options[select.selectedIndex].text;
        div.textContent = selectOption;
        div.style.background = "none";
        div.style.display = 'block';
        circle.style.display ='block';
    });
};

function selectFaculty() {
    const select = document.getElementById("faculty_education");
    const div = document.getElementById("grade_text_2");
    const circle = document.getElementById("grade_text_2__circle")
    select.addEventListener('change', function() {
        const selectOption = select.options[select.selectedIndex].text;
        div.textContent = selectOption;
        div.style.background = "none";
        div.style.display = 'block';
        circle.style.display ='block';
    });
};

function selectOp() {
    const select = document.getElementById("op_education");
    const div = document.getElementById("grade_text_3");
    const circle = document.getElementById("grade_text_3__circle")
    select.addEventListener('change', function() {
        const selectOption = select.options[select.selectedIndex].text;
        div.textContent = selectOption;
        div.style.background = "none";
        div.style.display = 'block';
        circle.style.display ='block';
    });
};

function postData() {
    const formData = new FormData(document.getElementById("registration_form"));
    formData.set('photo_ava', img);
    formData.set('password', formData.get('tg'))
    fetch('/register/user/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        document.getElementById("registration_form").reset();
        location.reload();
    })
    .catch(error => {
        if (response.status === 400) {
            for (const field in data.errors) {
                const errorField = document.getElementById(`${field}Error`);
                errorField.textContent = data.errors[field];
            }
        }
    });
}

function countDate() {
    const inputDate = document.getElementById("data");
    const ageInput = document.getElementById("age");
    const circle = document.getElementById("age_circle");
    inputDate.addEventListener('input', function() {
        let birthday = new Date(inputDate.value);
        let date = new Date();
        let year = "лет"
        let age = date.getFullYear() - birthday.getFullYear();
        if ((date.getMonth() < birthday.getMonth()) ||
            (date.getMonth() === birthday.getMonth() && date.getDate() < birthday.getDate())) {
                age--;
            };
        if (age % 10 === 1 && age % 100 != 11) {
            year = "год";
        } else if ((age % 10 < 5) && (age % 100 < 10 || age % 100 >= 20)){
            year = "года";
        }
        ageInput.textContent = age + " " + year;
        circle.style.display = "block";
    });
};

// Fetch and display items
// function fetchUser() {
//     fetch('/myapp/api/items/')
//     .then(response => response.json())
//     .then(data => {
//         const itemsList = document.getElementById("itemsList");
//         itemsList.innerHTML = '';

//         data.forEach(item => {
//             const row = itemsList.insertRow();
//             const nameCell = row.insertCell(0);
//             const descriptionCell = row.insertCell(1);
//             const priceCell = row.insertCell(2);
//             const activeCell = row.insertCell(3);

//             nameCell.textContent = item.name;
//             descriptionCell.textContent = item.description;
//             priceCell.textContent = item.price;
//             activeCell.textContent = item.is_active ? 'Yes' : 'No';
//         });
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// }

// window.onload = fetchUser;

uploadAva();
closePhoto();
correctNumber();
correctTg();
textToP();
buttonContinue();
employeeOrStudent();
textWork();
textWorkStudent();
grade();
selectLevelEducation();
selectFaculty();
selectOp();
sex();
nameTop();
countDate();