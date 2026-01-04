from playwright.sync_api import expect
import pytest


@pytest.mark.regression
@pytest.mark.authorization
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_page_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_page_title).to_be_visible()
    expect(courses_page_title).to_have_text('Courses')

    empty_state_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(empty_state_title).to_be_visible()
    expect(empty_state_title).to_have_text('There is no results')

    empty_state_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_state_description).to_be_visible()
    expect(empty_state_description).to_have_text('Results from the load test pipeline will be displayed here')
