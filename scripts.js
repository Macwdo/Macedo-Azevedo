async function get_jwt(username, password) {

    const headers = {
    'Content-Type': 'application/json'
    };

    const body = JSON.stringify({
        "username": `${username}`,
        "password": `${password}`
    })

    const config = {
        method: 'POST',
        headers: headers,
        body: body
    }

    const token = await fetch('https://gordinho.macedoweb.com.br/api/token/', config).then(
        objects => {
            return objects.json()
        }
    )    
    return token
}

async function listar() {

    const campo = "parteadv"

    const token = await get_jwt("", "")

    const headers = {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token.access}`
    };
    
    const config = {
        method: 'GET',
        headers: headers
    }

    const data = await fetch(`https://gordinho.macedoweb.com.br/api/v1/${campo}/`, config).then(
        response => {
            return response.json()
        }
    )
    
    console.log(data)
    return data


}



async function criar() {
    const headers = {
    'Content-Type': 'application/json',
    };

    const body = JSON.stringify({
        "nome": "",
        "email": "",
        "numero": ""
    })

    const config = {
        method: 'POST',
        headers: headers,
        body: body,
    }


    const response = await fetch('http://127.0.0.1:8000/api/v1/advogados/', config)
    const json = response.json()
    console.log(json)
    console.log(response.status)

}



function pegardado() {

}