function addkith() {
    fetch("index.cgi")
        .then(r => r.text())
        .then(html => {
            console.log(html);
            let e = document.createElement('li');
            e.innerHTML = html;
            document.getElementById('kith').appendChild(e);
        })
}
