run-test:

	. .venv/bin/activate && coverage run --source='.' manage.py test -v 2
	
