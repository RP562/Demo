import system

# Define the restart command based on the operating system
# For Windows
command = ["net", "stop", "Ignition", "&&", "net", "start", "Ignition"] #fdfdfdf


try:
    # Confirm the action
    response = system.gui.confirm("Are you sure you want to restart the Ignition Gateway?")
    if response:
        # Execute the command
        system.util.execute(command)
        system.gui.messageBox("Ignition Gateway is restarting. Please wait for it to come back online.")
except Exception as e:
    system.gui.errorBox("Failed to restart Ignition Gateway:\n{}".format(str(e)))