from Utopia import Utopia

print "Starting unit test for Utopia Module..."
print "Testing a non existent account..."

uto = Utopia("user1", "pass1")

assert uto.user == "user1", "Utopia.user did not match with arg1 for Utopia class"
assert uto.pwd == "pass1", "Utopia.pwd did not match with arg1 for Utopia class"
assert not uto.csrftoken, "Utopia.csrftoken was mutated. should be False by default"
assert not uto.last_url, "Utopia.last_url was mutated. should be False by default"
uto.login()
assert not uto.is_login(), "This should not be login coz account does not exist"
assert uto.csrftoken, "Utopia.csrftoken should have a value by now after trying to logg in."
assert uto.last_url, "Utopia.last_url should have a value by now after trying to log in."

print "pass"

print "Testing misc function"
assert uto.numerize("28,622")== 28622, "28,622 should not be "+uto.numerize("28,622")
print "pass"

print "Testing an existing account..."

#place username password here
uto = Utopia("", "")

#place username password here
assert uto.user == "", "Utopia.user did not match with arg1 for Utopia class"
assert uto.pwd == "", "Utopia.pwd did not match with arg1 for Utopia class"
assert not uto.csrftoken, "Utopia.csrftoken was mutated. should be False by default"
assert not uto.last_url, "Utopia.last_url was mutated. should be False by default"
uto.login()
assert uto.is_login(), "Utopia.is_login() should be True"
assert uto.csrftoken, "Utopia.csrftoken should have a value by now after logging in."
assert uto.last_url, "Utopia.last_url should have a value by now after logging in."

print "Now testing Utopia action..."
uto.update_sot()
assert type(uto.sot) == dict, "Utopia.sot shoud be a dictionary"
print "SOT"
for s in uto.sot:
    print s, ": ", uto.sot[s]
uto.logout()
assert not uto.is_login(), "uto.is_login() Should be false by now after logging out."
