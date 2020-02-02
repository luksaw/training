*** Variables ***

${BROWSER}  chrome
${URL}  https://www.mixesdb.com/db/index.php?title=Special:UserLogin

${USERNAME_INPUT}  //input[@id='wpName1']
${PASSWORD_INPUT}  //input[@id='wpPassword1']
${SUBMIT_BUTTON}  //input[@name='wpLoginAttempt']
${HEADER_AFTER_LOGIN}  //li[@id='pt-userpage']
${LOGIN_ERROR_MESSAGE}  //div[@class='errorbox']

${VALID_USERNAME}  test_username
${VALID_PASSWORD}  Passw0rd!
${INVALID_USERNAME}  invalid_username
${INVALID_PASSWORD}  1234556