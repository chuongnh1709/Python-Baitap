#!/usr/bin/env python3

__doc__ = '''
Chuẩn bị cho buổi sau
---------------------

- Cài đặt virtualenv, dùng nó tạo virtualenv cho Python3 (-p python3)
- Xem trong thư mục ``env`` vừa tạo có gì.
  https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments
- Activate môi trường vừa tạo, dùng pip cài đặt các thư viện phổ biến::

  ```
  pip install requests six flake8 ipython ipdb numpy pandas scipy scikit-learn matplotlib jupyter flask beautifulsoup4 requests-html
  pip install black # Python 3.6+ only
  ```
'''  # NOQA


def main():
    print(__doc__)


if __name__ == "__main__":
    main()
