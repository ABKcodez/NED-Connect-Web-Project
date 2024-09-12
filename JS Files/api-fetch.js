let options = {
    method: "POST",
    headers: {
        "Content-type": "application/json"
    },
    body: JSON.stringify({
        "user_id": 5,
        "first_name": "Arqam",
        "last_name": "Khursheed",
        "email": "arqamkhursheed123@gmail.com",
        "password": "arqam124",
        "contact": "03232720555",
        "category": "Student"
    })
}

// fetch('', options)
//     .then(response => response.json())
//     .then(json => console.log(json))


async function getUsersData(url){
    const response = await fetch(url);
    var data = await response.json();
    console.log(data[0]);
    }

getUsersData('http://127.0.0.1:8000/auth-data');
// console.log(myArray[1]);
// myArray = JSON.parse(data);
// let p = await   fetch('http://127.0.0.1:8000/')
// console.log(p);