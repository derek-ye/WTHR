module.exports = { 
  'Title Test': function(browser) {
    browser
      .url('http://127.0.0.1:5000/')
      .waitForElementVisible('body')
      .assert.title('WTHR')
      .saveScreenshot('./screenshots/title-test.png')
      .end();
  },
  'Page1 Search Test': function(browser) {
    browser
      .url('http://127.0.0.1:5000/')
      .setValue('input[type=text]', ['Fremont', browser.Keys.ENTER])
      .assert.containsText('#weekly-report', 'Weekly Report - Fremont, CA, USA')
      .saveScreenshot('./screenshots/p1-search-test.png')
      .end();
  },
  'Page2 Search Test': function(browser) {
    browser
      .url('http://127.0.0.1:5000/weatherdata')
      .setValue('input[type=text]', ['Wenzhou', browser.Keys.ENTER])
      .assert.containsText('#weekly-report', 'Wenzhou, Zhejiang, China')
      .saveScreenshot('./screenshots/p2-search-test.png')
      .end();
  },
};