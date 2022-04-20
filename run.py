import Base
import Splash

if __name__ == "__main__":
    # Run a system clear command, depending on your OS
    Splash.ClearScreen()

    # Output the splash title
    Splash.Title()

    # Output the current version of the script
    Splash.Version()

    # Check for updates
    CheckVersion.do()

    # Output the splash description
    Splash.Description()

    # Output the list of dependencies
    Splash.Dependencies()

    # Output the very hard and complex tutorial on how to use the dehasher
    Splash.Usage()

    # Delete the "temp/result" file, if it exists
    Base.clean()

    # Run the main script (the one that does the "dehashing")
    Base.main()
