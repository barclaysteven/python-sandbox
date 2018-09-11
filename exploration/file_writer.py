input = {
    "organization": "barclaysteven",
    "branch": "my-test"
}

file = open("test-file.json", "w")

file.write(str(input))
file.close()
