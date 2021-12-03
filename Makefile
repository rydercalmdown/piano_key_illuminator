PI_IP_ADDRESS=10.0.2.224
PI_USERNAME=pi

.PHONY: install
install:
	@cd scripts && bash install_pi.sh

.PHONY: copy
copy:
	@echo "For development only"
	@rsync -a $(shell pwd) --exclude env --exclude training $(PI_USERNAME)@$(PI_IP_ADDRESS):/home/$(PI_USERNAME)

.PHONY: shell
shell:
	@echo "For development only"
	@ssh $(PI_USERNAME)@$(PI_IP_ADDRESS)
 
 .PHONY: run
 run:
	@cd scripts && bash run_application.sh

.PHONY: ping
ping:
	@ping $(PI_IP_ADDRESS)
