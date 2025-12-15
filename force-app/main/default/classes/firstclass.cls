public class firstclass 
	{
public static void contactmethod()
{
    contact con = new contact();
    con.Firstname = 'Teju';
    con.LastName = 'Nandigama';
    con.MobilePhone = '7842852037';
    insert con;
    system.debug(con);
}
    public void casemethod()
    {
        case ca = new case();
        ca.Status = 'New';
        ca.origin = 'phone';
        insert ca;
        system.debug(ca);
    }
        public void leadmethod()
        { 
            lead l = new lead();
        l.lastname = 'eemani';
        l.status ='working-contacted';
            l.Company = 'accenture';
        insert l;
        system.debug(l);
        }
  
}