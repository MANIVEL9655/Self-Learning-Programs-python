import java.util.HashMap;
import java.util.Scanner;

public class ARPSimulation {
    private static HashMap<String, String> arpTable = new HashMap<>();

    private static void populateARPTTable() {
        arpTable.put("192.168.0.1", "00-14-22-01-23-45");
        arpTable.put("192.168.0.2", "00-14-22-01-23-46");
        arpTable.put("192.168.0.3", "00-14-22-01-23-47");
    }

    public static void main(String[] args) {
        populateARPTTable();
        Scanner scanner = new Scanner(System.in);
        System.out.println("ARP Protocol Simulation\nEnter 'exit' to quit.");

        while (true) {
            System.out.print("Enter IP address to resolve: ");
            String ipAddress = scanner.nextLine();
            if (ipAddress.equalsIgnoreCase("exit")) break;
            System.out.println("Resolved MAC Address: " + 
                arpTable.getOrDefault(ipAddress, "MAC Address not found"));
        }

        scanner.close();
        System.out.println("Exiting ARP Simulation. Goodbye!");
    }
}