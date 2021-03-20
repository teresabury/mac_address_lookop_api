
This program get a mac address as parameter and return Company Name associated with that MAC address.
To get an access to REST API, store api_key in env variable API_KEY

Program can be run on Docker with following commands:
$ docker build -t ex_1 .
$ docker run --rm  -e API_KEY=$API_KEY ex_1 <MAC_address>
$ docker run --rm  ex_1 -h (get the help about the program)
