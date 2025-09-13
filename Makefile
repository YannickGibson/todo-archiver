run:
	python todo_archiver.py
delete:
# ask for confirmation
	@read -p "Are you sure you want to delete the archive directory? (y/n) " choice; \
	if [ "$$choice" = "y" ]; then \
		rm -rf archive; \
		echo "Archive directory deleted or did not exist before."; \
	else \
		echo "Operation cancelled."; \
	fi
reset:
	@read -p "Are you sure you want to reset the TODO file? This will erase all current tasks. (y/n) " choice; \
	if [ "$$choice" = "y" ]; then \
		python reset.py; \
		echo "TODO file has been reset."; \
		$(MAKE) delete; \
	else \
		echo "Operation cancelled."; \
	fi
	