import urllib.request
import json

urls = [
    "http://api.open.notify.org/astros.json",
    "http://httpbin.org/get",
    "http//jsonplaceholder.typicode.com/posts"
    
]    

for url in urls:
    try:
        print(f"mencoba {url}...")
        response = urllib.request.urlopen(url, timeout=5)
        data_json = response.read().decode('utf-8')
        data = json.loads(data_json)
        print("berhasil\n")
        
        # tampilkan data sesusai url
        if "astros" in url:
            print(f"Astronaut di ISS: {data['number']} orang")
            for astronaut in data['people']:
                print(f" - {astronaut['name']}")
                
        elif "httpbin" in url:
            print(f"Origin IP: {data['origin']}")
        elif "jsonplaceholder" in url:
            print("contoh judul:", data[0]['title'])
        break
    except Exception as e:
        print(f"gagal: {e}\n")
        
else:
    print("semua url gagal. gunakan data lokal")
    data = [{"title": "Belajar API"}, {"title": "error handling"}, {"title": "logging"}]
    print("\ndata lokal:")
    for i, post in enumerate(data, start=1):
        print(f"{i}. {post['title']}")