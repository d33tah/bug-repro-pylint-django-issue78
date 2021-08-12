FROM python:3.9

ADD ./requirements.txt .
RUN python3 -m pip install -r requirements.txt

ADD ./pylint_django_no_member_repro pylint_django_no_member_repro/
ADD ./.pylintrc .

ENV DJANGO_SETTINGS_MODULE=pylint_django_no_member_repro.settings

ENTRYPOINT ["python3", "-m", "pylint", "pylint_django_no_member_repro"]
