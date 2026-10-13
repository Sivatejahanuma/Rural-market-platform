function fetchPrices() {
    fetch("http://127.0.0.1:5000/api/prices")
        .then(res => res.json())
        .then(data => {
            let html = "<h3>Market Prices</h3>";
            data.forEach(item => {
                html += `<p>${item.crop}: ₹${item.price}</p>`;
            });
            document.getElementById("price-list").innerHTML = html;
        });
}

function getAdvice() {
    const crop = document.getElementById("cropName").value;

    fetch("http://127.0.0.1:5000/api/advice", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({crop})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("advice").innerText = data.advice;
    });
}
