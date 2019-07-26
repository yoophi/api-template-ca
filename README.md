# api-template

API 서비스 개발을 위한 템플릿

TODO:

- [x] 환경에 따른 설정파일 적용 (prod, dev)
- [x] 환경변수에 따른 설정 적용 
- [ ] Newrelic 연동 

----

production:

```
export DATABASE_URI=mysql://user:pass@host:3306/database
export FLASK_APP=application
FLASK_CONFIG=production flask run

or 

FLASK_APP=app:create_app('production') flask run
```

development:

```
export DEV_DATABASE_URI=mysql://user:pass@host:3306/database
export FLASK_APP=application
FLASK_CONFIG=development flask run

or 

FLASK_APP=app:create_app('development') flask run
```
