def test_api(playwright):
    request = playwright.request.new_context()
    response = request.get("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status == 200

    body = response.json()
    print(body)
    assert body['id'] == 1
    request.dispose()