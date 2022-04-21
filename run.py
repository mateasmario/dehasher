import utils.Multiprocessing
import utils.Splash
import utils.Versioning

if __name__ == "__main__":
    # Run a system clear command, depending on your OS
    utils.Splash.ClearScreen()

    # Output the splash title
    utils.Splash.Title()

    # Output the current version of the script
    utils.Splash.Version()

    # Check for updates
    utils.Versioning.CheckVersion()

    # Output the splash description
    utils.Splash.Description()

    # Output the list of dependencies
    utils.Splash.Dependencies()

    # Output the very hard and complex tutorial on how to use the dehasher
    utils.Splash.Usage()

    # Delete the "temp/result" file, if it exists
    utils.Multiprocessing.Clean()

    # Run the script that waits for user input, creates the processes needed and tries to "dehash" the user input
    utils.Multiprocessing.CreateProcesses()
