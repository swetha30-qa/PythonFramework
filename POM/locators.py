

LOCATORS = {
    "search_home":('xpath','//button[@data-qa="shared-nav-search-button"]'),
    "enter_data":('xpath','//input[@type="search"]'),
    "search_button":('xpath','//button[@class="dtm-no-track jetstream-search__search-button"]')
}



LOCATORS_CAT = {
        "click_category":('xpath','//button[text()="{category}"]'),
        "click_subcategory":('xpath','//span[text()="{subcategory}"]'),
        "click_playstation":('xpath','//a[@aria-label="PlayStation.com"]'),
         "wait_games":('xpath','//button[text()="Games"]')
    }

LOCATORS_SOCIAL = {
    "move_element":('xpath','//span[text()="Follow us on social media"]'),
    "click_youtube":('xpath', '//img[@alt="YouTube"]'),
}

LOCATORS_REGION = {
    "change_region":('xpath','//div[text()=" Singapore "]'),
    "select_region":('xpath','//p[text()="India "]'),
    "wait_ele":('xpath','//p[contains(text(),"Europe, Middle East,")]'),
    "wait_element":('xpath','//span[text()="Sign In"]')
}



LOCATORS_PS5 = {
    "wait_ele":('xpath','//p[contains(text(),"Experience an all-new generation")]'),
    "move_ele" :('xpath','//p[contains(text(),"Experience an all-new generation")]'),
    "ps5":('xpath','//img[@alt="ps5 pro"]'),
    "click_ele":('xpath', '(//div[text()=" Find out more "])[2]')
}

LOCATORS_SIGNIN = {
    "click_signin":('xpath','//span[text()="Sign In"]'),
    "click_account":('xpath','//span[text()="Create an Account"]'),
    "click_create" :('xpath','//span[text()="Create"]'),
    "select_country":('xpath','//select[@name="country"]'),
    "click_country":('xpath','//select[@name="country"]'),
    "wait_ele":('xpath','//select[@aria-activedescendant="country__IN"]'),
    "click_lang":('xpath','//input[@data-dqa-text="language"]'),
    "click_next":('xpath','//div[@class="fitting-parent wrapper-centeralign"]'),
    "click_day":('xpath','(//div[@class="pulldown-wrapper"])[1]'),
    "select_date":('xpath','//select[@title="Day"]'),
    "option_date":('xpath','//option[@id="day__prompt-text"]'),
    "select_month":('xpath','//select[@title="Month"]'),
    "select_year":('xpath','//select[@title="Year"]')
}



LOCATORS_BANNER = {
    "click_banner":('xpath','//div[@data-slide="{slide_id}"]/../../../..//div[@data-slide-id="{next_slide_id}"]'),
    "click_slide":('xpath','//div[@data-slide="{next_slide_id}"]')
}

LOCATORS_GAMES = {
    "move_element":('xpath','//div[@data-slide="1"]'),
    "select_element":('xpath','//div[@data-slide="1"]'),
    "click_banner":('xpath','//div[@data-slide="1"]/../../../..//div[@data-slide-id="2"]'),
    "wait_deal":('xpath', '//h1[text()="January Sale"]'),
    "click_deal":('xpath', '(//div[@class="psw-product-tile psw-interactive-root"])[1]'),
    "wait_addtocart":('xpath', '//span[text()="Add to Cart"]')
}