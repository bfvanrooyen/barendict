from behave import given, when, then


@given('A user')
def given_a_user(context):
   pass


@when('The user visits http://www.barendict.com')
def when_the_user_visits(context):
    context.browser.get(context.test.live_server_url)


@then('The home page will load')
def then_the_home_page_will_load(context):
    assert 'Barend ICT' in context.browser.title

