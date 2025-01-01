fetch('https://dummyjson.com/api/', {
    method: 'GET',
    headers: {
        'Authorization': 'Bearer',
        'Content-Type': 'application/json'
    }
})
    .then(function (res) { return res.json(); })
    .then(console.log);
