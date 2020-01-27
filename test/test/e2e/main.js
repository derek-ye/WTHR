module.exports = { 
  'Title Test': function(browser) {
    browser
      .url('http://127.0.0.1:5000/')
      .waitForElementVisible('body')
      .assert.title('WTHR')
      .saveScreenshot('./screenshots/title-test.png')
      .end();
  },
  'Temperature Test': function(browser) {
    browser
      .url('http://127.0.0.1:5000/')
      .waitForElementVisible('body')
      .assert.title('WTHR')
      .saveScreenshot('./screenshots/temp-test.png')
      .end();
  },
};