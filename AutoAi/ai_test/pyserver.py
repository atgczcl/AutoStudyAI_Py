from bottle import route, run

@route('/')
def home():
    article = {'name': 'A Royal Baby', 'body': 'A slow news week'}
    return article

def main():
    run(host='localhost', port=8081)

if __name__ == '__main__':
    main()
