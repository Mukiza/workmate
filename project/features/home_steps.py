from lettuce import step, world
from project.features.pages.home import HomePage


@step(u'Given I am an anonymous user')
def given_i_am_an_anonymous_user(step):
    pass


@step(u'And I visit the home page')
def and_i_visit_the_home_page(step):
    world.page = HomePage(world.browser)
    world.page.visit()


@step(u'Then I should see the welcome text')
def then_i_should_see_the_welcome_text(step):
    world.page.is_text_present("Welcome to workmate")
