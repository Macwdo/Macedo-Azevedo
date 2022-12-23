async function get_jwt() {

    const password = ""
    const username = ""

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
    console.log(token.access)
    return token
}

async function listar() {

    const campo = ""

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

    const campo = ""
    const token = await get_jwt("", "")

    const headers = {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token.access}`
    };

    const body = JSON.stringify({
        'nome': 'dsasadasd',
        'email': 'dada@gmca',
        'numero': '2132131231',
        'cpf_cnpj': '9231019322',
        'registro': '2022-12-20',
        'tipo': 'PJ'
        })

    const config = {
        method: 'POST',
        headers: headers,
        body: body
    }


    const response = await fetch(`https://gordinho.macedoweb.com.br/api/v1/${campo}/`, config).then(
        object => {
            return object.json()
        }
    )

    console.log(response)
    console.log(response.status)

}



function pegardado() {

}