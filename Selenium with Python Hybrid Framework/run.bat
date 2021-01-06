pushd C:\Python\Courses\Selenium with Python Hybrid Framework
pytest -s -v test_cases\ --browser chrome --html=.\reports\report.html
rem pytest -s -v test_cases\ --browser firefox --html=.\reports\report.html
rem pytest -s -v -m "sanity" test_cases\ --browser chrome --html=.\reports\report.html
rem pytest -s -v -m "regression" test_cases\ --browser chrome --html=.\reports\report.html
