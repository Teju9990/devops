public class practice {

    public static String sayHello(String name) {
        return 'Hello ' + name;
    }

    // UPDATED method signature
    public static Account createAccount(String accountName, String email) {
        Account acc = new Account();
        acc.Name = accountName;
        acc.Customer_Email__c = email; // required field
        insert acc;
        return acc;
    }
}