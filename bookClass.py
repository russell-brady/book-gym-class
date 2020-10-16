import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time


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


def wait_until_slot_is_open(now, gym_slot):
    if gym_slot > now + timedelta(hours=24):
        print("Waiting for gym slot to open......")
        total_seconds = (gym_slot - (now + timedelta(hours=24))).total_seconds()
        # Add extra 2 seconds
        time.sleep(total_seconds + 2)


def get_course_id(request, gym_id, slot_start_date, gym_time):
    url = "https://myflye.flyefit.ie/myflye/book-workout/167/" + str(gym_id) + "/" + str(slot_start_date)
    get_slots_request = request.get(url)
    get_slots_request.raise_for_status()

    soup = BeautifulSoup(get_slots_request.content, features="html.parser")
    slot = soup.find(attrs={"data-course-time": gym_time})

    if slot is None:
        print("Slot is not available...")
        return

    course_id = slot['data-course-id']
    return course_id


def book_gym_slot(request, gym_id, gym_time):
    now = datetime.today()
    slot_start_time = gym_time.split(" ")[0]
    slot_start_date = (now + timedelta(days=1)).strftime("%Y-%m-%d")
    gym_slot = datetime.strptime(slot_start_date + "-" + slot_start_time, '%Y-%m-%d-%H:%M')

    wait_until_slot_is_open(now, gym_slot)

    course_id = get_course_id(request, gym_id, slot_start_date, gym_time)
    if course_id is None:
        return

    print('Booking gym slot for tomorrow...')

    post_url = 'https://myflye.flyefit.ie/api/course_book'
    data = {'course_id': course_id}

    book_slot_request = request.post(post_url, data)
    book_slot_request.raise_for_status()

    print('Successfully booked class...')
