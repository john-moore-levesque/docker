from behave import *
import re

# Go to a specified URL
@when(u'we go to "{url}"')
@given(u'we go to "{url}"')
def goToUrl(context, url):
    context.browser.browser.get(url)


# Check the current url
# Partial URL match (useful if you have a URL that contains a session ID)
@then(u'the current URL is "{currentUrl}"')
@then(u'the current URL contains "{currentUrl}"')
def checkUrl(context, currentUrl):
    assert re.search(currentUrl, context.browser.browser.current_url)
