import json  # NOQA
import os  # NOQA
import pickle  # NOQA
import yaml  # NOQA
import urllib.request


def get_element():
    '''Trả về số phần tử của kiểu dữ liệu sau khi dùng module `yaml` để load

    Thực hiện các yêu cầu tại ``__doc__``

    :rtype int:
    '''
    url = 'https://raw.githubusercontent.com/'
    url += 'hvnsweeting/states/master/salt/event/init.sls'
    name_file_downloaded = 'event.yaml'
    urllib.request.urlretrieve(url, name_file_downloaded)
    with open(name_file_downloaded, 'r') as f:
        yaml_file = yaml.safe_load(f)
    with open('event.json', 'w') as fp:
        json.dump(yaml_file, fp)
    with open('event.pkl', 'wb') as pkl:
        pickle.dump(yaml_file, pkl)
    print(os.stat(name_file_downloaded).st_size,
          os.stat('event.json').st_size,
          os.stat('event.pkl').st_size)

    result = yaml_file
    return result


def solve():
    '''Học viên không cần viết code trong hàm `solve`, chỉ thực hiện
    đổi tên lại function của mình cho phù hợp

    :rtype int:
    '''
    result = get_element()

    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()

