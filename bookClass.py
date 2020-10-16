import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


def create_request_session():
    print('Creating Session...')
    return requests.Session()


def login(request, email, password):
    print('Logging In...')
    login_data = {'email_address': email, 'password': password, 'log_in': 'Log+In'}
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/71.0.3578.98 Safari/537.36'}

    login = request.post("https://myflye.flyefit.ie/login", data=login_data, headers=headers)
    login.raise_for_status()

    print('Logged In Successfully...')


def book_gym_slot(request, gym_id, gym_time):
    time = gym_time.split(" ")[0].split(":")
    print(time)

    print('Booking gym slot for tomorrow...')

    tomorrow = datetime.today() + timedelta(days=1)
    tomorrow_formatted = tomorrow.strftime("%Y-%m-%d")

    url = "https://myflye.flyefit.ie/myflye/book-workout/167/" + str(gym_id) + "/" + str(tomorrow_formatted)
    print(url)

    r2 = request.get(url)
    r2.raise_for_status()

    soup = BeautifulSoup(r2.content, features="html.parser")
    slot = soup.find(attrs={"data-course-time": gym_time})

    if slot is None:
        print("Slot is not available...")
        return

    course_id = slot['data-course-id']

    post_url = 'https://myflye.flyefit.ie/api/course_book'
    data = {'course_id': course_id}

    r3 = request.post(post_url, data)
    r3.raise_for_status()

    print('Successfully booked class...')
