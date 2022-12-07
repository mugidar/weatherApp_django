document.addEventListener("DOMContentLoaded", function () {
    const submitBtn = document.querySelector('#submit')
    const inputField = document.querySelector('#city')
    const cities = document.querySelectorAll('.city_name')
    const error = document.querySelector('.error')
    let citiesArr = []
    cities.forEach((item) => {
        citiesArr.push(item.innerHTML.trim())
    })

    
    submitBtn.addEventListener('click', (e) => {
        if(citiesArr.includes(`${inputField.value}`)){
            e.preventDefault()
            inputField.style.borderColor = "red"
            error.innerHTML = "City already in list"
        }else if (inputField.value.length === 0) {
            console.log('0')
        }
       
    })
})