rm -rf build/ dist/ astars.egg-ingo/

python3 setup.py bdist_wheel

twine upload --repository testpypi dist/*
twine upload --repository pypi dist/*