from behave import *
from actions import getElement

# Check for an image with a specified source
@then(u'it has an image with the source "{source}"')
def checkForImage(context, source):
    myImage = getElement(context, "img", source)
    if myImage:
        return True
    else:
        return False

# Check the page title
@then(u'the title is "{title}"')
def checkPageTitle(context, title):
    assert context.browser.browser.title == title


# Check the page source for a testString
@then(u'it says "{testString}"')
def checkPageSource(context, testString):
    assert testString in context.browser.browser.page_source


# Check the page source for one of two possible test strings
@then(u'it says either "{testString1}" or "{testString2}"')
def checkPageSourceEither(context, testString1, testString2):
    assert testString1 in context.browser.browser.page_source or testString2 in context.browser.browser.page_source


# Check the page source for the ABSENCE of a testString
@then(u'it does NOT say "{testString}"')
def checkNotPageSource(context, testString):
    assert testString not in context.browser.browser.page_source


# Check for an element in the page
@then(u'it has a {thing} with the {identifier} "{thingname}"')
def checkForThing(context, thing, identifier, thingname):
    if "tag" in identifier.lower():
        assert context.browser.browser.find_elements_by_tag_name(thingname)
    elif "class" in identifier.lower():
        assert context.browser.browser.find_elements_by_class_name(thingname)
    elif "name" in identifier.lower():
        assert context.browser.browser.find_element_by_name(thingname)
    elif "xpath" in identifier.lower():
        assert context.browser.browser.find_element_by_xpath(thingname)
    else:
        assert context.browser.browser.find_element_by_id(thingname)


# Switch to a different frame
@when(u'we switch to "{frame}"')
@given(u'we switch to "{frame}"')
def switchToFrame(context, frame):
    context.browser.browser.switch_to_frame(frame)


# Switch to the main body
@when(u'we switch to the main body')
@given(u'we switch to the main body')
def switchToMain(context):
    context.browser.browser.switch_to_default_content()
