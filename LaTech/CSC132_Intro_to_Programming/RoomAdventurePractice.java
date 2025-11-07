// Import the Scanner class from the java.util package. 
// We need this to get user input from the console.
import java.util.Scanner;

// Define the main class for our game. 
// This class will "run" the game and manage the game state.
public class RoomAdventure{

    // === CLASS VARIABLES (GAME STATE) ===
    // These are `static`, meaning they belong to the *class* itself, not an object.
    // There is only ONE copy of these for the whole game (they are "shared").

    // This holds the *Room object* the player is currently in. It's our 'player location'.
    private static Room currentRoom;
    // This is the player's inventory, a fixed-size array of 5 slots.
    // We initialize it with `null` values, which we'll use to mean "empty slot".
    private static String[] inventory = {null, null, null, null, null};
    // A helper variable to pass messages (like "You took the key") from our 
    // 'handler' methods back to the main loop to be printed.
    private static String status;

    // === CONSTANTS ===
    // A `final` variable is a constant; its value cannot be changed after it's set.
    // We use this for our default error message.
    final private static String DEFAULT_STATUS = "Sorry, I do not understand. Try [verb] [noun]. Valid verbs include 'go', 'look', and 'take'.";

    // === MAIN METHOD (The Game Engine) ===
    // This is the "entry point" of our program. 
    // The `public static void main` signature is required by Java to run a file.
    public static void main(String[] args){
        
        // Call our "world builder" method once at the beginning to create all 
        // our Room objects and link them together.
        setupGame();

        // This is the MAIN GAME LOOP. `while(true)` creates an infinite loop.
        // Each pass through this loop represents one "turn" for the player.
        while (true){
            // === 1. DISPLAY STATUS ===
            // Print the current room's details. This automatically calls the 
            // `toString()` method on the `currentRoom` object.
            System.out.println(currentRoom.toString());
            // Print the "Inventory:" label. `print` does not add a newline at the end.
            System.out.print("Inventory: ");

            // Use a standard `for` loop to print each item in the inventory array.
            // `inventory.length` is a *property* (not a method) of the array.
            for (int i = 0; i < inventory.length; i++){
                // Access the item at index `i` and print it, followed by a space.
                System.out.print(inventory[i] + " ");
            }

            // Print the player prompt. `\n` creates a newline for spacing.
            System.out.println("\nWhat would you like to do? ");
        

            // === 2. GET USER INPUT ===
            // Create a new `Scanner` object to read from `System.in` (the keyboard).
            // *Lecture Note: Creating a `new Scanner` inside a loop is bad practice!
            // We should create it *once* before the `while(true)` loop.
            Scanner s = new Scanner(System.in);
            // `s.nextLine()` pauses the program and waits for the user to type a line 
            // and press Enter. The text is stored in the `input` variable.
            String input = s.nextLine();
            
            // === 3. PARSE THE INPUT ===
            // This is our "parser". We split the `input` string by spaces.
            // e.g., "go east" becomes the array `{"go", "east"}`
            String[] words = input.split(" ");

            // A simple check to see if the user typed exactly two words.
            if (words.length != 2){
                // If not, set the status to the error message.
                status = DEFAULT_STATUS;
                // *Lecture Note: This is a bug! The code continues on.
                // If the user types "go", `words.length` is 1, this runs, but 
                // the *next line* will crash the program.
            }

            // Assume the first word (at index 0) is the command/verb.
            String verb = words[0];
            // Assume the second word (at index 1) is the target/noun.
            // *Lecture Note: BUG HERE! If `words.length` was 1, this line will 
            // throw an `ArrayIndexOutOfBoundsException` and crash!
            String noun = words[1];

            // === 4. HANDLE THE COMMAND ===
            // A `switch` statement is a clean way to check one variable against
            // multiple possible string values.
            switch (verb){
                // If the `verb` matches the string "go"...
                case "go":
                    // ...call our `handleGo` method, passing the `noun` (e.g., "east").
                    handleGo(noun);
                    // `break` is essential to exit the `switch` block.
                    break;
                // If the `verb` matches "look"...
                case "look":
                    // ...call our `handleLook` method.
                    handleLook(noun);
                    break;
                // If the `verb` matches "take"...
                case "take":
                    // ...call our `handleTake` method.
                    handleTake(noun);
                    break;
                // The `default` case runs if the `verb` matches none of the above.
                default: status = DEFAULT_STATUS;
            }
            
            // === 5. PRINT THE RESULT ===
            // After the handler method has run, print the `status` message 
            // (which is either a success or error message).
            System.out.println(status);
            
        } // Closes `while (true)` loop

    } // Closes `main` method

    // === "go" COMMAND HANDLER ===
    // A `private static` method. `private` = only this class can call it.
    // `static` = it belongs to the class, not an object.
    private static void handleGo(String noun){
        // Get the list of exit *commands* (e.g., "east") from the current room.
        String[] exitDirections = currentRoom.getExitDirections();
        // Get the list of *destinations* (e.g., `room2` object) from the current room.
        // These are "parallel arrays".
        
        Room[] exitDestinations = currentRoom.getExitDestinations();
        // Set a default "pessimistic" status. We assume the command will fail.
        status = "I don't see that room.";
        // Loop through all the possible exit directions.
        for (int i = 0; i < exitDirections.length; i++){
            // Check if the `noun` (what the user typed) equals the direction at this index.
            // *Must* use `.equals()` to compare String content, not `==`.
            if (noun.equals(exitDirections[i])){
                // If it matches, we move! Change the `static currentRoom` variable...
                // ...to the `Room` object at the *same index* in the destinations array.
                // *Lecture Note: BUG HERE! This is where the `go south` crash happens.
                // `exitDirections[1]` is "south", but `exitDestinations[1]` doesn't exist!
                currentRoom = exitDestinations[i];
                // Update the `status` to a success message.
                status = "Changed Room";
            } // Closes `if`
        } // Closes `for`
    } // Closes `handleGo`

    // === "look" COMMAND HANDLER ===
    private static void handleLook(String noun){
        // Get the list of items (e.g., "desk") from the current room.
        String[] items = currentRoom.getItems();
        // Get the parallel array of item *descriptions*.
        String[] itemDescriptions = currentRoom.getItemDescriptions();
        // Set a default failure status.
        status = "I don't see that item.";
        // Loop through all the `items`.
        for (int i = 0; i < items.length; i++){
            // If the `noun` matches the item name at this index...
            if (noun.equals(items[i])){
                // ...set the `status` to that item's *description*.
                status = itemDescriptions[i];
            } // Closes `if`
        } // Closes `for`
    } // Closes `handleLook`

    // === "take" COMMAND HANDLER ===
    private static void handleTake(String noun){
        // Get the list of *grabbable* items from the current room.
        String[] grabbables = currentRoom.getGrabbables();
        // Set a default failure status.
        status = "I can't grab that.";
        // Loop through all the `grabbables`.
        for (int i = 0; i < grabbables.length; i++){
            // If the `noun` matches a grabbable item...
            if (noun.equals(grabbables[i])){
                // ...we need to add it to inventory. Start a *nested loop* // to find the first empty (`null`) slot.
                for (int j = 0; j < inventory.length; j++){
                    // Check if this slot (`inventory[j]`) is empty.
                    // We *can* use `==` to check for `null`.
                    if (inventory[j] == null){
                        // If it's empty, put the item's name (`noun`) in this slot.
                        inventory[j] = noun;
                        // Set the success message.
                        status = "Added it to the inventory";
                        // **Crucial:** `break` out of the *inner* loop (`j` loop).
                        // If we don't, we'll add the item to *every* empty slot.
                        break;
                    } // Closes `if (inventory[j] == null)`
                } // Closes `for (int j...)` (inventory loop)
            } // Closes `if (noun.equals...)`
        } // Closes `for (int i...)` (grabbables loop)
    } // Closes `handleTake`

    // === WORLD BUILDER METHOD ===
    private static void setupGame(){
        // **Instantiation**: We are creating an *instance* (an object) of the `Room` 
        // class by calling its *constructor*.
        Room room1 = new Room("Room 1"); 
        // Create a second `Room` object.
        Room room2 = new Room("Room 2");

        // --- Setup for Room 1 ---
        // Create a local array of strings for `room1`'s exit commands.
        String[] room1ExitDirections = {"east", "south"};
        // Create a local array of `Room` objects for `room1`'s destinations.
        // *Lecture Note: THIS IS THE BUG!* // `room1ExitDirections` has 2 items (length=2).
        // `room1ExitDestinations` has 1 item (length=1).
        // This mismatch causes the `go south` crash.
        
        Room[]   room1ExitDestinations = {room2};

        // Create a local array for `room1`'s items.
        String[] room1Items = {"chair", "desk"};
        // Create the parallel array for `room1`'s item descriptions.
        String[] room1ItemDescriptions = {
            "It is a chair", 
            "Its a desk, there is a key on it."
        };
        // Create the array of grabbable items for `room1`.
        String[] room1Grabbables = {"key"};

        // Use the `room1` object's public "setter" method to pass the local 
        // `room1ExitDirections` array *into* the object.
        room1.setExitDirections(room1ExitDirections);
        // Pass the destinations array into the object.
        room1.setExitDestinations(room1ExitDestinations);
        // Pass the items array into the object.
        room1.setItems(room1Items);
        // Pass the item descriptions array into the object.
        room1.setItemDescriptions(room1ItemDescriptions);
        // Pass the grabbables array into the object.
        room1.setGrabbables(room1Grabbables);

        // --- Setup for Room 2 ---
        // Create exit directions for `room2`.
        String[] room2ExitDirections = {"west"};
        // Create exit destinations for `room2`. The "west" exit links back to `room1`.
        Room[]   room2ExitDestinations = {room1};
        // Create items for `room2`.
        String[] room2Items = {"fireplace", "rug"};
        // Create item descriptions for `room2`.
        String[] room2ItemDescriptions = {
            "Its on fire", 
            "There is a lump of coal on the rug."
        };
        // Create grabbable items for `room2`.
        String[] room2Grabbables = {"coal"};
        // Use the `room2` object's "setter" methods to load all its data.
        room2.setExitDirections(room2ExitDirections);
        room2.setExitDestinations(room2ExitDestinations);
        room2.setItems(room2Items);
        room2.setItemDescriptions(room2ItemDescriptions);
        room2.setGrabbables(room2Grabbables);

        // --- Set Starting Room ---
        // Set the *global* `static` variable `currentRoom` to point to `room1`.
        // This is the player's starting location.
        currentRoom = room1;
    } // Closes `setupGame`
} // Closes `RoomAdventure` class

// === ROOM CLASS (The Blueprint) ===
// This class is a "blueprint" for a Room. It doesn't *do* anything on its own.
// Its job is to *hold data* about a single location.
class Room{

    // === INSTANCE VARIABLES ===
    // These are *not* `static`. Every `Room` object gets its *own separate copy* // of these variables.
    // `private` means they can only be accessed by methods *inside* this `Room` class.
    
    // The room's name.
    private String name;
    // The list of exit commands (e.g., "north", "south").
    private String[] exitDirections;    
    // The list of `Room` objects where those exits lead.
    private Room[] exitDestinations;
    // The list of items you can see in the room.
    private String[] items;
    // The list of descriptions for those items.
    private String[] itemDescriptions;
    // The list of items you can "take" from the room.
    private String[] grabbables;

    // === CONSTRUCTOR ===
    // A "constructor" is a special method that runs when `new Room(...)` is called.
    // It *must* have the same name as the class and *no* return type.
    // Its job is to initialize the object's variables.
    public Room(String name){
        // `this.name` refers to the *instance variable* (the one at the top).
        // `name` refers to the *parameter* that was passed in.
        // This line assigns the parameter value to the instance variable.
        
        this.name = name; 
    } // Closes `Room` constructor

    // === GETTERS AND SETTERS ===
    // These are public "gatekeeper" methods used to access the `private` variables.
    // This is a core OOP concept called "Encapsulation".
    

    // A "setter" method. It's `public` so other classes can call it.
    // It's `void` because it doesn't return a value.
    public void setExitDirections(String[] exitDirections){
        // `this.exitDirections` (instance var) = `exitDirections` (parameter).
        this.exitDirections = exitDirections;
    } // Closes `setExitDirections`
    
    // A "getter" method. It's `public` and `returns` the data type.
    public String[] getExitDirections(){
        // It simply returns the value of the private instance variable.
        // `this.` is not needed here because there's no name conflict.
        return exitDirections;
    } // Closes `getExitDirections`
    
    // Setter for `exitDestinations`
    public void setExitDestinations(Room[] exitDestinations){
        this.exitDestinations = exitDestinations;
    }

    // Getter for `exitDestinations`
    public Room[] getExitDestinations(){
        return exitDestinations;
    }

    // Setter for `items`
    public void setItems(String[] items){
        this.items = items;
    }

    // Getter for `items`
    public String[] getItems(){
        return items;
    }
    
    // Setter for `itemDescriptions`
    public void setItemDescriptions(String[] itemDescriptions){
        this.itemDescriptions = itemDescriptions;
    }

    // Getter for `itemDescriptions`
    public String[] getItemDescriptions(){
        return itemDescriptions;
    }

    // Getter for `grabbables`
    public String[] getGrabbables(){
        return grabbables;
    }

    // Setter for `grabbables`
    public void setGrabbables(String[] grabbables){
        this.grabbables = grabbables;
    }

    // === toString METHOD ===
    // This is a special method that Java calls automatically
    // anytime you try to print a `Room` object (e.g., `System.out.println(room1)`).
    // Its job is to return a `String` that represents the object.
    public String toString(){
        // Create a local variable `result` to build our string.
        String result = "----------\n";
        // Append the location name.
        result += "Location: " + name;

        // Append the "You See:" label.
        result += "\nYou See: ";
        // Use a standard `for` loop to go through the `items` array.
        for (int i = 0; i < items.length; i++){
            // Append each item name and a space.
            result += items[i] + " ";
        }

        // Append the "Exits:" label.
        result += "\nExits: ";
        // Use an "enhanced for-each loop".
        // This reads as: "For each `String` (which we will call `direction`) 
        // *in* the `exitDirections` array..."
        
        for (String direction : exitDirections){
            // Append each direction and a space.
            result += direction + " ";
        }

        // Return the final, fully-built string.
        return result + "\n";
    } // Closes `toString`
} // Closes `Room` class