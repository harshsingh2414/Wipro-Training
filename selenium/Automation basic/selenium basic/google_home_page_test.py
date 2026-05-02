from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager

browser_choice = input("Which browser do you want to use? (chrome/edge): ").strip().lower()

if browser_choice == "chrome":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browser_choice == "edge":
    edge_driver_path = r"C:\wipro training\selenium\Automation basic\resource\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(executable_path=edge_driver_path))
else:
    raise ValueError("Invalid choice! Please enter 'chrome' or 'edge'.")

driver.get("https://www.google.com")
pagetitle = driver.title

if pagetitle == "Google":
    print("Google homepage loaded - Pass")
else:
    print("Google homepage not loaded - Fail")

driver.quit()
