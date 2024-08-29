import threading
import requests
import time
import uuid



def downloader(url, name):
    print(f"Starting Downloading {name}")
    response = requests.get(url)
    with open(f'{str(uuid.uuid4()).split('-')[0]}.jpg', 'wb') as f:
        f.write(response.content)
    print(f"Finished Downloading {name}")

if __name__ == "__main__":
    urls = [
        "https://plus.unsplash.com/premium_photo-1723741320347-bf8a65518f8e?w=600&auto=format&fit=crop&q=70&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHx8cHJlbWl1bXx8fHwwfHx8fHw%3D",
        "https://images.unsplash.com/photo-1721332155637-8b339526cf4c?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "https://images.unsplash.com/photo-1721332155433-3a4b5446bcd9?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "https://plus.unsplash.com/premium_photo-1722851534029-31a83a992dc6?q=80&w=1374&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "https://images.unsplash.com/photo-1723902499824-13f225769ebf?q=80&w=1374&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    ]
    
    start_time = time.time()
    processes = []
    for i, url in enumerate(urls):
        p=threading.Thread(target=downloader,args=[url,i])
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
    
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
