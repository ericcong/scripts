PROJECT_NAME = $(shell pwd | xargs basename)
all:
	-@mkdir __tmp__
	-@mkdir __tmp__/__build__
	-@find src -name "*.java" > __tmp__/__srcs__.tmp
	-@find lib -name "*.jar" > __tmp__/__libs__.tmp
	-@sed 's/^/ /' __tmp__/__libs__.tmp > __tmp__/__libs_lines__.tmp && mv __tmp__/__libs_lines__.tmp __tmp__/__libs__.tmp
	-@sed 's/$$/ /' __tmp__/__libs__.tmp > __tmp__/__libs_lines__.tmp && mv __tmp__/__libs_lines__.tmp __tmp__/__libs__.tmp
	-@echo "Class-path:\c" | cat - __tmp__/__libs__.tmp > __tmp__/__libs_body__.tmp && mv __tmp__/__libs_body__.tmp __tmp__/__libs__.tmp
	-@javac -classpath "lib/*" -sourcepath src -d __tmp__/__build__ @__tmp__/__srcs__.tmp
	-@jar cmfe __tmp__/__libs__.tmp $(PROJECT_NAME).jar $(PROJECT_NAME) lib -C __tmp__/__build__ . -C src assets
	-@rm -r __tmp__