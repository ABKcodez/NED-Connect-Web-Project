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

fetch('http://127.0.0.1:8000/auth-data', options)
    .then(response => response.json())
    .then(json => console.log(json))


let p = fetch('http://127.0.0.1:8000/auth-data', {
    headers: {
        'Accept': 'application/json'
    }
})
    let response = p.response();
    console.log(response.text());

    console.log(text)
// let p = await   fetch('http://127.0.0.1:8000/')
// console.log(p);