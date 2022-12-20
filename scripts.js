async function get_jwt() {
    console.clear()

    const headers = {
    'Content-Type': 'application/json'
    };

    const body = JSON.stringify({
        "username": "",
        "password": ""
    })

    const config = {
        method: 'POST',
        headers: headers,
        body: body
    }

    const response = await fetch('https://gordinho.macedoweb.com.br/api/token/', config).then(
        objects => {
            return objects.json()
        }
    )
    console.log(response.access)
    console.log(response)
    return response.access
}

async function listar_advogado() {

    const headers_token = {
        'Content-Type': 'application/json'
        };
    
        const body = JSON.stringify({
            "username": "",
            "password": ""
        })
    
        const config_token = {
            method: 'POST',
            headers: headers_token,
            body: body
        }
    
        const response_token = await fetch('http://127.0.0.1:8000/api/token/', config_token).then(
            objects => {
                return objects.json()
            }
        )


    const headers = {
    'authorization':`Bearer ${response_token.access}`
    }

    const config = {
        method: 'GET',
        headers: headers,
    }


    const response = await fetch('http://127.0.0.1:8000/api/v1/processos/', config).then(
        objects => {
            return objects.json()
        }
    )
    console.log(response, response.length)

}


async function criar_advogado() {
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

    document.getElementById
}