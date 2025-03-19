import mysql.connector
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def connect_to_db():
    try :
            return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gym"
        )
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None  

class MemberManagement:
    def add_member(self, name, age, gender, username, password, contact_number):
        
        db = connect_to_db()
        cursor = db.cursor()

        query = "INSERT INTO members (name, age, gender, username, password, contact_number) VALUES (%s, %s, %s, %s, %s, %s)"
        try:
            cursor.execute(query, (name, age, gender,
                           username, password, contact_number))
            db.commit()
            print("Member added successfully!")
        except mysql.connector.IntegrityError:
            print("Error: Username already exists.")

        cursor.close()
        db.close()
    def update_member(self, member_id, name=None, age=None, gender=None, contact_number=None):
        db = connect_to_db()
        cursor = db.cursor()

        query = "UPDATE members SET "
        values = []

        if name:
            query += "name = %s, "
            values.append(name)
        if age:
            query += "age = %s, "
            values.append(age)
        if gender:
            query += "gender = %s, "
            values.append(gender)
        if contact_number:
            query += "contact_number = %s, "
            values.append(contact_number)

        if not values:  # If no fields were provided, return an error message
            print("No updates provided. Please enter at least one field to update.")
            return

        query = query.rstrip(", ") + " WHERE member_id = %s"
        values.append(member_id)

        cursor.execute(query, tuple(values))
        db.commit()
        
        if cursor.rowcount > 0:
            print("Member details updated successfully!")
        else:
            print("Error: Member ID not found.")

        cursor.close()
        db.close()

    def delete_member(self, member_id):
        db = connect_to_db()
        cursor = db.cursor()
        
        # Check if member exists
        check_query = "SELECT * FROM members WHERE member_id = %s"
        cursor.execute(check_query, (member_id,))
        member = cursor.fetchone()
        
        if member:
            query = "DELETE FROM members WHERE member_id = %s"
            cursor.execute(query, (member_id,))
            db.commit()
            print("Member deleted successfully!")
        else:
            print("Error: Member ID not found.")
        
        cursor.close()
        db.close()
    def view_all_members(self):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT * FROM members"
        cursor.execute(query)
        members = cursor.fetchall()

        for member in members:
            print(member)

        cursor.close()
        db.close()

    def view_member_by_id(self, member_id):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT * FROM members WHERE member_id = %s"
        cursor.execute(query, (member_id,))
        member = cursor.fetchone()

        if member:
            print(member)
        else:
            print("Member not found.")

        cursor.close()
        db.close()

class WorkoutPlanManagement:
    def add_workout_plan(self, name, description, duration_weeks, difficulty_level):
        db = connect_to_db()
        cursor = db.cursor()

        query = "INSERT INTO workout_plans (workout_plan_name, description, duration_weeks, difficulty_level) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, description,
                       duration_weeks, difficulty_level))
        db.commit()
        print("Workout plan added successfully!")

        cursor.close()
        db.close()

   
    def update_workout_plan(self, plan_id, name=None, description=None, duration_weeks=None, difficulty_level=None):
        db = connect_to_db()
        cursor = db.cursor()

        # Check if the workout plan exists
        cursor.execute("SELECT * FROM workout_plans WHERE workout_plan_id = %s", (plan_id,))
        plan = cursor.fetchone()

        if not plan:
            print("Error: Workout Plan ID not found.")
            cursor.close()
            db.close()
            return

        query = "UPDATE workout_plans SET "
        values = []

        if name:
            query += "workout_plan_name = %s, "
            values.append(name)
        if description:
            query += "description = %s, "
            values.append(description)
        if duration_weeks:
            query += "duration_weeks = %s, "
            values.append(duration_weeks)
        if difficulty_level:
            query += "difficulty_level = %s, "
            values.append(difficulty_level)

        query = query.rstrip(", ") + " WHERE workout_plan_id = %s"
        values.append(plan_id)

        cursor.execute(query, tuple(values))
        db.commit()
        print("Workout plan updated successfully!")

        cursor.close()
        db.close()

    def delete_workout_plan(self, plan_id):
        db = connect_to_db()
        cursor = db.cursor()

        # Check if the workout plan exists
        cursor.execute("SELECT * FROM workout_plans WHERE workout_plan_id = %s", (plan_id,))
        plan = cursor.fetchone()

        if not plan:
            print("Error: Workout Plan ID not found.")
            cursor.close()
            db.close()
            return

        query = "DELETE FROM workout_plans WHERE workout_plan_id = %s"
        cursor.execute(query, (plan_id,))
        db.commit()
        print("Workout plan deleted successfully!")

        cursor.close()
        db.close()

        db = connect_to_db()
        cursor = db.cursor()

        query = "DELETE FROM workout_plans WHERE workout_plan_id = %s"
        cursor.execute(query, (plan_id,))
        db.commit()
        print("Workout plan deleted successfully!")

        cursor.close()
        db.close()

    def view_all_workout_plans(self):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT * FROM workout_plans"
        cursor.execute(query)
        plans = cursor.fetchall()

        for plan in plans:
            print(plan)

        cursor.close()
        db.close()

    def view_workout_plan_by_id(self, plan_id):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT * FROM workout_plans WHERE workout_plan_id = %s"
        cursor.execute(query, (plan_id,))
        plan = cursor.fetchone()

        if plan:
            print(plan)
        else:
            print("Workout plan not found.")

        cursor.close()
        db.close()

  
    def assign_workout_plan_to_member(self, member_id, plan_id):
        db = connect_to_db()
        cursor = db.cursor()

        # Check if the member exists
        cursor.execute("SELECT * FROM members WHERE member_id = %s", (member_id,))
        member = cursor.fetchone()
        
        # Check if the workout plan exists
        cursor.execute("SELECT * FROM workout_plans WHERE workout_plan_id = %s", (plan_id,))
        plan = cursor.fetchone()
        
        # Check if the workout plan is already assigned
        cursor.execute("SELECT * FROM member_workout_plans WHERE member_id = %s AND workout_plan_id = %s", (member_id, plan_id))
        existing_assignment = cursor.fetchone()

        if not member:
            print("Error: Member ID not found.")
        elif not plan:
            print("Error: Workout Plan ID not found.")
        elif existing_assignment:
            print("Workout plan already assigned to this member. Details:")
            print(existing_assignment)
        else:
            query = "INSERT INTO member_workout_plans (member_id, workout_plan_id, assigned_date) VALUES (%s, %s, CURDATE())"
            cursor.execute(query, (member_id, plan_id))
            db.commit()
            print("Workout plan assigned successfully!")

        cursor.close()
        db.close()

    def view_assigned_workout_plan(self,member_id):
            db = connect_to_db()
            cursor = db.cursor()
            
            query = "SELECT w.workout_plan_name, w.description, w.duration_weeks, w.difficulty_level FROM workout_plans w JOIN member_workout_plans mw ON w.workout_plan_id = mw.workout_plan_id WHERE mw.member_id = %s"
            cursor.execute(query, (member_id,))
            plan = cursor.fetchone()

            # Fetch all remaining results before closing the cursor
            cursor.fetchall()  

            if plan:
                print(f"\nWorkout Plan:\nName: {plan[0]}\nDescription: {plan[1]}\nDuration: {plan[2]} weeks\nDifficulty: {plan[3]}")
            else:
                print("No workout plan assigned.")

            cursor.close()
            db.close()

class MembershipManagement:
    def add_membership(self, member_id, membership_type, start_date, duration_months):
        db = connect_to_db()
        cursor = db.cursor()

        # Check if membership already exists for the member
        check_query = "SELECT * FROM memberships WHERE member_id = %s"
        cursor.execute(check_query, (member_id,))
        existing_membership = cursor.fetchone()

        if existing_membership:
            print("Membership already available for this member. Details:")
            print(existing_membership)
            cursor.close()
            db.close()
            return

        # Define membership prices based on type
        membership_prices = {
            "Gold": 4000.00,
            "Silver": 2000.00,
            "Bronze": 1000.00
        }

        # Get the price of the selected membership type
        price = membership_prices[membership_type]

        expiry_date = datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=duration_months * 30)
        query = "INSERT INTO memberships (member_id, membership_type, start_date, expiry_date, price) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (member_id, membership_type, start_date, expiry_date.strftime("%Y-%m-%d"), price))
        db.commit()
        print("Membership added successfully!")

        cursor.close()
        db.close()

    def update_membership(self, membership_id, membership_type=None, start_date=None, duration_months=None):
        db = connect_to_db()
        cursor = db.cursor()

        query = "UPDATE memberships SET "
        values = []

        if membership_type:
            query += "membership_type = %s, "
            values.append(membership_type)
        if start_date:
            query += "start_date = %s, "
            values.append(start_date)
        if duration_months:
            query += "expiry_date = DATE_ADD(start_date, INTERVAL %s MONTH), "
            values.append(duration_months)

        query = query.rstrip(", ") + " WHERE membership_id = %s"
        values.append(membership_id)

        cursor.execute(query, tuple(values))
        db.commit()
        print("Membership updated successfully!")

        cursor.close()
        db.close()

    def delete_membership(self, membership_id):
        db = connect_to_db()
        cursor = db.cursor()

        # Check if membership exists
        check_query = "SELECT * FROM memberships WHERE membership_id = %s"
        cursor.execute(check_query, (membership_id,))
        membership = cursor.fetchone()

        if membership:
            query = "DELETE FROM memberships WHERE membership_id = %s"
            cursor.execute(query, (membership_id,))
            db.commit()
            print("Membership deleted successfully!")
        else:
            print("Error: Membership ID not found.")

        cursor.close()
        db.close()
    def view_all_memberships(self):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT * FROM memberships"
        cursor.execute(query)
        memberships = cursor.fetchall()

        for membership in memberships:
            print(membership)

        cursor.close()
        db.close()

    def view_membership_by_id(self, membership_id):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT * FROM memberships WHERE membership_id = %s"
        cursor.execute(query, (membership_id,))
        membership = cursor.fetchone()

        if membership:
            print(membership)
        else:
            print("Membership not found.")

        cursor.close()
        db.close()

    def renew_membership(self, membership_id, additional_months):
        db = connect_to_db()
        cursor = db.cursor()

        # Check if membership exists
        check_query = "SELECT * FROM memberships WHERE membership_id = %s"
        cursor.execute(check_query, (membership_id,))
        membership = cursor.fetchone()

        if membership:
            query = "UPDATE memberships SET expiry_date = DATE_ADD(expiry_date, INTERVAL %s MONTH) WHERE membership_id = %s"
            cursor.execute(query, (additional_months, membership_id))
            db.commit()
            print("Membership renewed successfully!")
        else:
            print("Error: Membership ID not found.")

        cursor.close()
        db.close()
    
    def track_membership_expiry(self, member_id):
        db = connect_to_db()
        cursor = db.cursor()

        # Check if member exists
        check_query = "SELECT * FROM members WHERE member_id = %s"
        cursor.execute(check_query, (member_id,))
        member = cursor.fetchone()

        if not member:
            print("Error: Member ID not found.")
            cursor.close()
            db.close()
            return

        # Check if membership exists
        query = "SELECT expiry_date FROM memberships WHERE member_id = %s"
        cursor.execute(query, (member_id,))
        membership = cursor.fetchall()

        if membership:
            print(f"Membership expiry date: {membership[0]}")
        else:
            print("No active membership found for this member.")

        cursor.close()
        db.close()

          
    def check_membership_status(self,member_id):
        db = connect_to_db()
        cursor = db.cursor()
        query = "SELECT membership_type, expiry_date FROM memberships WHERE member_id = %s"
        cursor.execute(query, (member_id,))
        membership = cursor.fetchone()
        
        if membership:
            status = "Active" if membership[1] >= datetime.now().date() else "Expired"
            print(f"\nMembership Type: {membership[0]}\nExpiry Date: {membership[1]}\nStatus: {status}")
        else:
            print("No active membership found.")
        
        cursor.close()
        db.close()

class TrainerManagement:
    def add_trainer(self, name, specialization, username, password, contact_number):
        db = connect_to_db()
        cursor = db.cursor()

        query = "INSERT INTO trainers (name, specialization, username, password, contact_number) VALUES (%s, %s, %s, %s, %s)"
        try:
            cursor.execute(query, (name, specialization,
                           username, password, contact_number))
            db.commit()
            print("Trainer added successfully!")
        except mysql.connector.IntegrityError:
            print("Error: Username already exists.")

        cursor.close()
        db.close()

    def update_trainer(self, trainer_id, name=None, specialization=None, contact_number=None):
        db = connect_to_db()
        cursor = db.cursor()

        query = "UPDATE trainers SET "
        values = []

        if name:
            query += "name = %s, "
            values.append(name)
        if specialization:
            query += "specialization = %s, "
            values.append(specialization)
        if contact_number:
            query += "contact_number = %s, "
            values.append(contact_number)

        query = query.rstrip(", ") + " WHERE trainer_id = %s"
        values.append(trainer_id)

        cursor.execute(query, tuple(values))
        db.commit()
        print("Trainer details updated successfully!")

        cursor.close()
        db.close()

    def delete_trainer(self, trainer_id):
        db = connect_to_db()
        cursor = db.cursor()

        check_query = "SELECT * FROM trainers WHERE trainer_id = %s"
        cursor.execute(check_query, (trainer_id,))
        trainer = cursor.fetchone()

        if trainer:
            query = "DELETE FROM trainers WHERE trainer_id = %s"
            cursor.execute(query, (trainer_id,))
            db.commit()
            print("Trainer deleted successfully!")
        else:
            print("Error: Trainer ID not found.")

        cursor.close()
        db.close()

    def view_all_trainers(self):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT * FROM trainers"
        cursor.execute(query)
        trainers = cursor.fetchall()

        for trainer in trainers:
            print(trainer)

        cursor.close()
        db.close()

    def view_trainer_by_id(self, trainer_id):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT * FROM trainers WHERE trainer_id = %s"
        cursor.execute(query, (trainer_id,))
        trainer = cursor.fetchone()

        if trainer:
            print(trainer)
        else:
            print("Trainer not found.")

        cursor.close()
        db.close()

    def assign_trainer_to_member(self, trainer_id, member_id):
        db = connect_to_db()
        cursor = db.cursor()
        
        # Check if trainer exists
        cursor.execute("SELECT * FROM trainers WHERE trainer_id = %s", (trainer_id,))
        trainer = cursor.fetchone()
        
        # Check if member exists
        cursor.execute("SELECT * FROM members WHERE member_id = %s", (member_id,))
        member = cursor.fetchone()
        
        if trainer and member:
            query = "UPDATE members SET trainer_id = %s WHERE member_id = %s"
            cursor.execute(query, (trainer_id, member_id))
            db.commit()
            print("Trainer assigned to member successfully!")
        else:
            if not trainer:
                print("Error: Trainer ID not found.")
            if not member:
                print("Error: Member ID not found.")
        
        cursor.close()
        db.close()
        
    def view_assigned_members(self, trainer_id):
         db = connect_to_db()
         cursor = db.cursor()

         query = """
            SELECT member_id, name, age, gender, username, contact_number, status 
            FROM members 
            WHERE trainer_id = %s
        """
         cursor.execute(query, (trainer_id,))
         members = cursor.fetchall()

         if members:
            print("\n--- Assigned Members ---")
            for member in members:
                print(f"ID: {member[0]}, Name: {member[1]}, Age: {member[2]}, Gender: {member[3]}, Username: {member[4]}, Contact: {member[5]}, Status: {member[6]}")
         else:
            print("No members assigned to this trainer.")

         cursor.close()
         db.close()

class PaymentManagement:
    def record_payment(self, member_id, amount, payment_method, payment_date):
        db = connect_to_db()
        cursor = db.cursor()

        # Check if the member exists
        cursor.execute("SELECT * FROM members WHERE member_id = %s", (member_id,))
        member = cursor.fetchone()

        if not member:
            print("Error: Member ID not found.")
            cursor.close()
            db.close()
            return

        query = "INSERT INTO payments (member_id, amount, payment_method, payment_date) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (member_id, amount, payment_method, payment_date))
        db.commit()
        print("Payment recorded successfully!")

        cursor.close()
        db.close()

    def view_all_payments(self):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT * FROM payments"
        cursor.execute(query)
        payments = cursor.fetchall()

        for payment in payments:
            print(payment)

        cursor.close()
        db.close()

    def view_payment_by_id(self, payment_id):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT * FROM payments WHERE payment_id = %s"
        cursor.execute(query, (payment_id,))
        payment = cursor.fetchone()

        if payment:
            print(payment)
        else:
            print("Error: Payment ID not found.")

        cursor.close()
        db.close()

    def view_member_payment_history(self, member_id):
        db = connect_to_db()
        cursor = db.cursor()

        # Check if the member exists
        cursor.execute("SELECT * FROM members WHERE member_id = %s", (member_id,))
        member = cursor.fetchone()

        if not member:
            print("Error: Member ID not found.")
            cursor.close()
            db.close()
            return

        query = "SELECT * FROM payments WHERE member_id = %s"
        cursor.execute(query, (member_id,))
        payments = cursor.fetchall()

        if payments:
            for payment in payments:
                print(payment)
        else:
            print('single payment not even done my this member')

        cursor.close()
        db.close()

    def generate_payment_receipt(self, payment_id):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT member_id, amount, payment_method, payment_date FROM payments WHERE payment_id = %s"
        cursor.execute(query, (payment_id,))
        payment = cursor.fetchone()

        if payment:
            print(
                f"\nPayment Receipt\n---------------------\nMember ID: {payment[0]}\nAmount: {payment[1]}\nMethod: {payment[2]}\nDate: {payment[3]}\nThank you!\n")
        else:
            print("Error: Payment ID not found.")

        cursor.close()
        db.close()

class ReportAndAnalysis:
    def generate_member_report(self):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT gender, COUNT(*) FROM members GROUP BY gender"
        cursor.execute(query)
        data = cursor.fetchall()

        labels = [row[0] for row in data]
        sizes = [row[1] for row in data]

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['blue', 'pink', 'gray'])
        plt.title("Gender Distribution of Members")
        plt.show()

        cursor.close()
        db.close()


    def payment_report(self):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT members.name, SUM(payments.amount) FROM payments JOIN members ON payments.member_id = members.member_id GROUP BY members.name"
        cursor.execute(query)
        data = cursor.fetchall()

        names = [row[0] for row in data]
        amounts = [row[1] for row in data]

        plt.figure(figsize=(10, 5))
        plt.bar(names, amounts, color='orange')
        plt.xlabel("Member Name")
        plt.ylabel("Total Payments")
        plt.title("Payments Made by Members")
        plt.xticks(rotation=45)
        plt.show()

        cursor.close()
        db.close()

    def monthly_revenue(self):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT MONTH(payment_date), SUM(amount) FROM payments GROUP BY MONTH(payment_date)"
        cursor.execute(query)
        data = cursor.fetchall()

        months = [row[0] for row in data]
        revenues = [row[1] for row in data]

        plt.figure(figsize=(10, 5))
        plt.bar(months, revenues, color='purple')
        plt.xlabel("Month")
        plt.ylabel("Total Revenue")
        plt.title("Monthly Revenue Report")
        plt.xticks(months)
        plt.show()

        cursor.close()
        db.close()

    def inactive_member_report(self):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT name FROM members WHERE member_id NOT IN (SELECT DISTINCT member_id FROM attendance WHERE attendance_date >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH))"
        cursor.execute(query)
        data = cursor.fetchall()

        names = [row[0] for row in data]
        counts = len(names)

        plt.figure(figsize=(6, 6))
        plt.bar(['Inactive Members'], [counts], color='red')
        plt.xlabel("Status")
        plt.ylabel("Number of Inactive Members")
        plt.title("Inactive Members Report (Last 1 Month)")
        plt.show()

        cursor.close()
        db.close()

class EquipmentManagement:
    def add_equipment(self, name, equipment_type, quantity, condition):
        db = connect_to_db()
        cursor = db.cursor()

        query = "INSERT INTO equipment (name, equipment_type, quantity, equipment_condition) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (name, equipment_type, quantity, condition))
        db.commit()
        print("Equipment added successfully!")

        cursor.close()
        db.close()

    def update_equipment(self, equipment_id, name=None, equipment_type=None, quantity=None, condition=None):
        db = connect_to_db()
        cursor = db.cursor()

        # Check if equipment exists
        cursor.execute("SELECT * FROM equipment WHERE equipment_id = %s", (equipment_id,))
        equipment = cursor.fetchone()
        if not equipment:
            print("Error: Equipment ID not found.")
            cursor.close()
            db.close()
            return

        query = "UPDATE equipment SET "
        values = []

        if name:
            query += "name = %s, "
            values.append(name)
        if equipment_type:
            query += "equipment_type = %s, "
            values.append(equipment_type)
        if quantity:
            query += "quantity = %s, "
            values.append(quantity)
        if condition:
            query += "`condition` = %s, "
            values.append(condition)

        query = query.rstrip(", ") + " WHERE equipment_id = %s"
        values.append(equipment_id)

        cursor.execute(query, tuple(values))
        db.commit()
        print("Equipment details updated successfully!")

        cursor.close()
        db.close()

    def delete_equipment(self, equipment_id):
        db = connect_to_db()
        cursor = db.cursor()

        # Check if equipment exists
        cursor.execute("SELECT * FROM equipment WHERE equipment_id = %s", (equipment_id,))
        equipment = cursor.fetchone()
        if not equipment:
            print("Error: Equipment ID not found.")
            cursor.close()
            db.close()
            return

        query = "DELETE FROM equipment WHERE equipment_id = %s"
        cursor.execute(query, (equipment_id,))
        db.commit()
        print("Equipment deleted successfully!")

        cursor.close()
        db.close()

    def view_all_equipment(self):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT * FROM equipment"
        cursor.execute(query)
        equipment = cursor.fetchall()

        for item in equipment:
            print(item)

        cursor.close()
        db.close()

    def view_equipment_by_id(self, equipment_id):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT * FROM equipment WHERE equipment_id = %s"
        cursor.execute(query, (equipment_id,))
        equipment = cursor.fetchone()

        if equipment:
            print(equipment)
        else:
            print("Equipment not found.")

        cursor.close()
        db.close()

    def track_equipment_condition(self):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT equipment_condition, COUNT(*) FROM equipment GROUP BY equipment_condition"
        cursor.execute(query)
        data = cursor.fetchall()

        labels = [row[0] for row in data]
        counts = [row[1] for row in data]

        plt.figure(figsize=(6, 6))
        plt.pie(counts, labels=labels, autopct='%1.1f%%',
                colors=['green', 'yellow', 'red'])
        plt.title("Equipment Condition Status")
        plt.show()

        cursor.close()
        db.close()

class FeedbackManagement:
    def add_feedback(self, member_id, rating, feedback_text):
        db = connect_to_db()
        cursor = db.cursor()

        # Check if member exists
        cursor.execute("SELECT * FROM members WHERE member_id = %s", (member_id,))
        member = cursor.fetchone()
        if not member:
            print("Error: Member ID not found.")
            cursor.close()
            db.close()
            return

        query = "INSERT INTO feedback (member_id, rating, feedback_text) VALUES (%s, %s, %s)"
        cursor.execute(query, (member_id, rating, feedback_text))
        db.commit()
        print("Feedback submitted successfully!")

        cursor.close()
        db.close()

    def update_feedback(self, feedback_id, rating=None, feedback_text=None):
        db = connect_to_db()
        cursor = db.cursor()

        # Check if feedback exists
        cursor.execute("SELECT * FROM feedback WHERE feedback_id = %s", (feedback_id,))
        feedback = cursor.fetchone()
        if not feedback:
            print("Error: Feedback ID not found.")
            cursor.close()
            db.close()
            return

        query = "UPDATE feedback SET "
        values = []

        if rating:
            query += "rating = %s, "
            values.append(rating)
        if feedback_text:
            query += "feedback_text = %s, "
            values.append(feedback_text)

        query = query.rstrip(", ") + " WHERE feedback_id = %s"
        values.append(feedback_id)

        cursor.execute(query, tuple(values))
        db.commit()
        print("Feedback updated successfully!")

        cursor.close()
        db.close()

    def delete_feedback(self, feedback_id):
        db = connect_to_db()
        cursor = db.cursor()

        # Check if feedback exists
        cursor.execute("SELECT * FROM feedback WHERE feedback_id = %s", (feedback_id,))
        feedback = cursor.fetchone()
        if not feedback:
            print("Error: Feedback ID not found.")
            cursor.close()
            db.close()
            return

        query = "DELETE FROM feedback WHERE feedback_id = %s"
        cursor.execute(query, (feedback_id,))
        db.commit()
        print("Feedback deleted successfully!")

        cursor.close()
        db.close()

    def view_all_feedback(self):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT * FROM feedback"
        cursor.execute(query)
        feedbacks = cursor.fetchall()

        for feedback in feedbacks:
            print(feedback)

        cursor.close()
        db.close()

    def view_feedback_by_id(self, feedback_id):
        db = connect_to_db()
        cursor = db.cursor()

        query = "SELECT * FROM feedback WHERE feedback_id = %s"
        cursor.execute(query, (feedback_id,))
        feedback = cursor.fetchone()

        if feedback:
            print(feedback)
        else:
            print("Feedback not found.")

        cursor.close()
        db.close()

   
    def view_feedback_by_member(self, member_id):
        db = connect_to_db()
        cursor = db.cursor()

        # Check if member exists
        cursor.execute("SELECT * FROM members WHERE member_id = %s", (member_id,))
        member = cursor.fetchone()
        if not member:
            print("Error: Member ID not found.")
            cursor.close()
            db.close()
            return

        

        # Check if member exists
        cursor.execute("SELECT * FROM members WHERE member_id = %s", (member_id,))
        member = cursor.fetchone()
        if not member:
            print("Error: Member ID not found.")
            cursor.close()
            db.close()
            return

        query = "SELECT * FROM feedback WHERE member_id = %s"
        cursor.execute(query, (member_id,))
        feedbacks = cursor.fetchall()

        if feedbacks:
            for feedback in feedbacks:
                print(feedback)
        else:
            print('feedback is not given by this member')

        cursor.close()
        db.close()

class Admin:
    def __init__(self, admin_id):
        self.admin_id = admin_id
        
    def admin_show_options(self):
        while True:
            print("\n--- Admin Panel ---")
            print("1. Manage Members")
            print("2. Manage Trainers")
            print("3. Manage Memberships")
            print("4. Manage Workout Plans")
            print("5. Manage Payments")
            print("6. Manage Equipment")
            print("7. Manage Feedback")
            print("8. Generate Reports")
            print("9. Exit")

            choice = input("Enter choice: ")
            if choice == '1':
                self.manage_members()
            elif choice == '2':
                self.manage_trainers()
            elif choice == '3':
                self.manage_memberships()
            elif choice == '4':
                self.manage_workout_plans()
            elif choice == '5':
                self.manage_payments()
            elif choice == '6':
                self.manage_equipment()
            elif choice == '7':
                self.manage_feedback()
            elif choice == '8':
                self.generate_reports()
            elif choice == '9':
                print("Exiting Admin Panel...")
                break
            else:
                print("Invalid choice. Try again.")

    def manage_members(self):
        member_manager = MemberManagement()
        while True:
            print("\n--- Manage Members ---")
            print("1. Add Member")
            print("2. Update Member")
            print("3. Delete Member")
            print("4. View All Members")
            print("5. View Member by ID")
            print("6. Exit")

            choice = input("Enter choice: ")
            if choice == '1':
                print("\n--- Add New Member ---")
                name = input("Enter Name: ")
                age = input("Enter Age: ")
                gender = input("Enter Gender (Male/Female/Other): ")
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                contact_number = int(input("Enter Contact Number: "))
                member_manager.add_member(name, age, gender, username, password, contact_number)
            elif choice == '2':
                 member_id = input("Enter Member ID: ")
                 name = input("Enter new Name (or leave blank to keep current): ") or None
                 age = input("Enter new Age (or leave blank to keep current): ") or None
                 gender = input("Enter new Gender (or leave blank to keep current): ") or None
                 contact_number = input("Enter new Contact Number (or leave blank to keep current): ") or None
                 member_manager.update_member(member_id, name, age, gender, contact_number)
            elif choice == '3':
                member_id = input("Enter Member ID to delete: ")
                member_manager.delete_member(member_id)

            elif choice == '4':
                member_manager.view_all_members()
            elif choice == '5':
                member_id = input("Enter Member ID to view: ")
                member_manager.view_member_by_id(member_id)
            elif choice == '6':
                print("Exiting Member Management...")
                break
            else:
                print("Invalid choice. Try again.")

    def manage_trainers(self):
        trainer_manager = TrainerManagement()

        while True:
            print("\n--- Trainer Management ---")
            print("1. Add Trainer")
            print("3. Delete Trainer")
            print("4. View All Trainers")
            print("5. View Trainer by ID")
            print("6. Assign Trainer to Member")
            print("7. View Assigned Members")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter Name: ")
                specialization = input("Enter Specialization: ")
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                contact_number = input("Enter Contact Number: ")
                trainer_manager.add_trainer(name, specialization, username, password, contact_number)

            
            elif choice == '3':
                trainer_id = input("Enter Trainer ID to delete: ")
                trainer_manager.delete_trainer(trainer_id)

            elif choice == '4':
                trainer_manager.view_all_trainers()

            elif choice == '5':
                trainer_id = input("Enter Trainer ID to view: ")
                trainer_manager.view_trainer_by_id(trainer_id)

            elif choice == '6':
                trainer_id = input("Enter Trainer ID: ")
                member_id = input("Enter Member ID: ")
                trainer_manager.assign_trainer_to_member(trainer_id, member_id)

            elif choice == '7':
                trainer_id = input("Enter Trainer ID to view assigned members: ")
                trainer_manager.view_assigned_members(trainer_id)

            elif choice == '8':
                print("Exiting Trainer Management...")
                break

            
    def manage_memberships(self):
       membership_manager = MembershipManagement()

       while True:
        print("\n--- Membership Management ---")
        print("1. Add Membership")
        print("2. Update Membership")
        print("3. Delete Membership")
        print("4. View All Memberships")
        print("5. View Membership by ID")
        print("6. Renew Membership")
        print("7. Track Membership Expiry")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            member_id = input("Enter Member ID: ")
            membership_type = input("Enter Membership Type: ")
            start_date = input("Enter Start Date (YYYY-MM-DD): ")
            duration_months = int(input("Enter Duration (in months): "))
            membership_manager.add_membership(member_id, membership_type, start_date, duration_months)

        elif choice == '2':
            membership_id = input("Enter Membership ID: ")
            membership_type = input("Enter new Membership Type (or leave blank): ") or None
            start_date = input("Enter new Start Date (YYYY-MM-DD) (or leave blank): ") or None
            duration_months = input("Enter additional months (or leave blank): ")
            duration_months = int(duration_months) if duration_months else None
            membership_manager.update_membership(membership_id, membership_type, start_date, duration_months)

        elif choice == '3':
            membership_id = input("Enter Membership ID to delete: ")
            membership_manager.delete_membership(membership_id)

        elif choice == '4':
            membership_manager.view_all_memberships()

        elif choice == '5':
            membership_id = input("Enter Membership ID to view: ")
            membership_manager.view_membership_by_id(membership_id)

        elif choice == '6':
            membership_id = input("Enter Membership ID to renew: ")
            additional_months = int(input("Enter additional months: "))
            membership_manager.renew_membership(membership_id, additional_months)

        elif choice == '7':
            member_id = input("Enter Member ID to check expiry: ")
            membership_manager.track_membership_expiry(member_id)

        elif choice == '8':
            print("Exiting Membership Management...")
            break

        else:
            print("Invalid choice. Try again.")
    
    def manage_workout_plans(self):
        manager = WorkoutPlanManagement()

        while True:
            print("\n--- Workout Plan Management ---")
            print("1. Add Workout Plan")
            print("2. Update Workout Plan")
            print("3. Delete Workout Plan")
            print("4. View All Workout Plans")
            print("5. View Workout Plan by ID")
            print("6. Assign Workout Plan to Member")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter workout plan name: ")
                description = input("Enter description: ")
                duration_weeks = int(input("Enter duration in weeks: "))
                difficulty_level = input("Enter difficulty level (Beginner/Intermediate/Advanced): ")
                manager.add_workout_plan(name, description, duration_weeks, difficulty_level)
            
            elif choice == '2':
                plan_id = input("Enter Workout Plan ID to update: ")
                name = input("Enter new name (or leave blank): ") or None
                description = input("Enter new description (or leave blank): ") or None
                duration_weeks = input("Enter new duration in weeks (or leave blank): ")
                duration_weeks = int(duration_weeks) if duration_weeks else None
                difficulty_level = input("Enter new difficulty level (or leave blank): ") or None
                manager.update_workout_plan(plan_id, name, description, duration_weeks, difficulty_level)
            
            elif choice == '3':
                plan_id = input("Enter Workout Plan ID to delete: ")
                manager.delete_workout_plan(plan_id)
            
            elif choice == '4':
                manager.view_all_workout_plans()
            
            elif choice == '5':
                plan_id = input("Enter Workout Plan ID to view: ")
                manager.view_workout_plan_by_id(plan_id)
            
            elif choice == '6':
                member_id = input("Enter Member ID: ")
                plan_id = input("Enter Workout Plan ID: ")
                manager.assign_workout_plan_to_member(member_id, plan_id)
            
            elif choice == '7':
                print("Exiting Workout Plan Management...")
                break
            
            else:
                print("Invalid choice. Try again.")

    def manage_payments(self):
         manager = PaymentManagement()

         while True:
            print("\n--- Payment Management ---")
            print("1. Record Payment")
            print("2. View All Payments")
            print("3. View Payment by ID")
            print("4. View Member Payment History")
            print("5. Generate Payment Receipt")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                member_id = input("Enter Member ID: ")
                amount = float(input("Enter Amount: "))
                payment_method = input("Enter Payment Method: ")
                payment_date = input("Enter Payment Date (YYYY-MM-DD): ")
                manager.record_payment(member_id, amount, payment_method, payment_date)
            
            elif choice == '2':
                manager.view_all_payments()
            
            elif choice == '3':
                payment_id = input("Enter Payment ID: ")
                manager.view_payment_by_id(payment_id)
            
            elif choice == '4':
                member_id = input("Enter Member ID: ")
                manager.view_member_payment_history(member_id)
            
            elif choice == '5':
                payment_id = input("Enter Payment ID: ")
                manager.generate_payment_receipt(payment_id)
            elif choice == '6':
                print("Exiting Payment Management...")
                break
            else:
                print("Invalid choice. Try again.")

    def manage_equipment(self):
        manager = EquipmentManagement()

        while True:
            print("\n--- Equipment Management ---")
            print("1. Add Equipment")
            print("2. Update Equipment")
            print("3. Delete Equipment")
            print("4. View All Equipment")
            print("5. View Equipment by ID")
            print("6. Track Equipment Condition")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter equipment name: ")
                equipment_type = input("Enter equipment type: ")
                quantity = int(input("Enter quantity: "))
                condition = input("Enter condition (Good/Needs Repair/Out of Order): ")
                manager.add_equipment(name, equipment_type, quantity, condition)
            
            elif choice == '2':
                equipment_id = input("Enter Equipment ID to update: ")
                name = input("Enter new name (or leave blank): ") or None
                equipment_type = input("Enter new type (or leave blank): ") or None
                quantity = input("Enter new quantity (or leave blank): ")
                quantity = int(quantity) if quantity else None
                condition = input("Enter new condition (or leave blank): ") or None
                manager.update_equipment(equipment_id, name, equipment_type, quantity, condition)
            
            elif choice == '3':
                equipment_id = input("Enter Equipment ID to delete: ")
                manager.delete_equipment(equipment_id)
            
            elif choice == '4':
                manager.view_all_equipment()
            
            elif choice == '5':
                equipment_id = input("Enter Equipment ID to view: ")
                manager.view_equipment_by_id(equipment_id)
            
            elif choice == '6':
                manager.track_equipment_condition()
            
            elif choice == '7':
                print("Exiting Equipment Management...")
                break
            
            else:
                print("Invalid choice. Try again.")

    def manage_feedback(self):
        manager = FeedbackManagement()

        while True:
            print("\n--- Feedback Management ---")
            print("1. Add Feedback")
            print("2. Update Feedback")
            print("3. Delete Feedback")
            print("4. View All Feedback")
            print("5. View Feedback by ID")
            print("6. View Feedback by Member ID")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                member_id = input("Enter Member ID: ")
                rating = int(input("Enter Rating (1-5): "))
                feedback_text = input("Enter Feedback: ")
                manager.add_feedback(member_id, rating, feedback_text)
            
            elif choice == '2':
                feedback_id = input("Enter Feedback ID to update: ")
                rating = input("Enter new rating (or leave blank): ")
                rating = int(rating) if rating else None
                feedback_text = input("Enter new feedback text (or leave blank): ") or None
                manager.update_feedback(feedback_id, rating, feedback_text)
            
            elif choice == '3':
                feedback_id = input("Enter Feedback ID to delete: ")
                manager.delete_feedback(feedback_id)
            
            elif choice == '4':
                manager.view_all_feedback()
            
            elif choice == '5':
                feedback_id = input("Enter Feedback ID to view: ")
                manager.view_feedback_by_id(feedback_id)
            
            elif choice == '6':
                member_id = input("Enter Member ID to view feedback: ")
                manager.view_feedback_by_member(member_id)
            
            elif choice == '7':
                print("Exiting Feedback Management...")
                break
            
            else:
                print("Invalid choice. Try again.")

                print("\n--- Manage Feedback ---")
                print("1. Delete Feedback")
                print("2. View All Feedback")
                print("3. View Feedback by ID")
                print("4. Exit")
                
                choice = input("Enter choice: ")
                
                if choice == '1':
                    feedback_id = input("Enter Feedback ID to delete: ")
                    feedback_manager.delete_feedback(feedback_id)
                elif choice == '2':
                    feedback_manager.view_all_feedback()
                elif choice == '3':
                    feedback_id = input("Enter Feedback ID to view: ")
                    feedback_manager.view_feedback_by_id(feedback_id)
                elif choice == '4':
                    print("Exiting Feedback Management...")
                    break
                else:
                    print("Invalid choice. Try again.")

    def generate_reports(self):
        manager = ReportAndAnalysis()

        while True:
            print("\n--- Report and Analysis ---")
            print("1. Generate Member Report")
            print("2. Payment Report")
            print("3. Monthly Revenue Report")
            print("4. Inactive Members Report")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                manager.generate_member_report()
           
            elif choice == '2':
                manager.payment_report()
            elif choice == '3':
                manager.monthly_revenue()
            elif choice == '4':
                manager.inactive_member_report()
            elif choice == '5':
                print("Exiting Report and Analysis...")
                break
            else:
                print("Invalid choice. Try again.")

class Member:
    def __init__(self,member_id):
       self.member_id=member_id
    def member_show_options(self):
        
        while True:
            print("\n--- Member Dashboard ---")
            print("1. View Profile")
            print("2. Update Profile")
            print("3. Check Membership Status")
            print("4. View Payment History")
            print("5. View Assigned Workout Plan")
            print("6. Give Feedback")
            print('7.view feedbacks ')
            print("8. Exit")
            
            choice = input("Enter your choice: ")
            member = MemberManagement()
            membership=MembershipManagement()
            payment=PaymentManagement()
            workout=WorkoutPlanManagement()
            feedback=FeedbackManagement()
            if choice == '1':
                member.view_member_by_id(self.member_id)
            elif choice == '2':
                name = input("Enter new Name (or leave blank to keep current): ") or None
                age = input("Enter new Age (or leave blank to keep current): ") or None
                gender = input("Enter new Gender (or leave blank to keep current): ") or None
                contact_number = input("Enter new Contact Number (or leave blank to keep current): ") or None
                member.update_member(self.member_id, name, age, gender, contact_number)
            elif choice == '3':
                membership.check_membership_status(self.member_id)
            elif choice == '4':
                payment.view_member_payment_history(self.member_id)
            elif choice == '5':
                workout.view_assigned_workout_plan(self.member_id)
            elif choice == '6':
                rating = int(input("Enter Rating (1-5): "))
                feedback_text = input("Enter Feedback: ")
                feedback.add_feedback(self.member_id, rating, feedback_text)
            elif choice == '8':
                print("Exiting Member Dashboard...")
                break
            elif choice=='7':
                feedback.view_feedback_by_member(self.member_id)
                
            else:
                print("Invalid choice. Try again.")

class Trainer:

   
    def view_profile(self):
        db = connect_to_db()
        cursor = db.cursor()
        query = "SELECT name, specialization, contact_number FROM trainers WHERE trainer_id = %s"
        cursor.execute(query, (self.trainer_id,))
        profile = cursor.fetchone()
        
        if profile:
            print("\nTrainer Profile:")
            print(f"Name: {profile[0]}\nSpecialization: {profile[1]}\nContact: {profile[2]}")
        else:
            print("Error: Profile not found.")
        
        cursor.close()
        db.close()
    def update_profile(self):
        db = connect_to_db()
        cursor = db.cursor()
        
        new_contact = input("Enter new contact number (or press Enter to skip): ") or None
        new_password = input("Enter new password (or press Enter to skip): ") or None
        
        values = []
        query = "UPDATE trainers SET "

        if new_contact:
            query += "contact_number = %s, "
            values.append(new_contact)
        if new_password:
            query += "password = %s, "
            values.append(new_password)

        if not values:  # If no values to update, show message and return
            print("No updates provided.")
            cursor.close()
            db.close()
            return

        query = query.rstrip(", ") + " WHERE trainer_id = %s"
        values.append(self.trainer_id)

        cursor.execute(query, tuple(values))
        db.commit()
        print("Profile updated successfully!")

        cursor.close()
        db.close()

   
    def view_member_progress(self):
            db = connect_to_db()
            cursor = db.cursor()
            query = "SELECT m.name, w.workout_plan_name, mw.assigned_date FROM members m JOIN member_workout_plans mw ON m.member_id = mw.member_id JOIN workout_plans w ON mw.workout_plan_id = w.workout_plan_id WHERE m.trainer_id = %s"
            cursor.execute(query, (self.trainer_id,))
            progress = cursor.fetchall()
            
            if progress:
                print("\nMember Workout Progress:")
                for p in progress:
                    print(f"Member: {p[0]}, Workout Plan: {p[1]}, Assigned Date: {p[2]}")
            else:
                print("No workout progress available.")
            
            cursor.close()
            db.close()

    def give_feedback_on_members(self):
            db = connect_to_db()
            cursor = db.cursor()
            
            member_id = input("Enter Member ID: ")
            feedback_text = input("Enter feedback: ")
            
            query = "INSERT INTO feedback (member_id, trainer_id, feedback_text) VALUES (%s, %s, %s)"
            cursor.execute(query, (member_id, self.trainer_id, feedback_text))
            db.commit()
            print("Feedback submitted successfully!")
            
            cursor.close()
            db.close()

    # def view_assigned_members(self):
    #     db = connect_to_db()
    #     cursor = db.cursor()
    #     query = "SELECT member_id, name, contact_number FROM members WHERE trainer_id = %s"
    #     cursor.execute(query, (self.trainer_id,))
    #     members = cursor.fetchall()
        
    #     if members:
    #         print("\nAssigned Members:")
    #         for member in members:
    #             print(f"ID: {member[0]}, Name: {member[1]}, Contact: {member[2]}")
    #     else:
    #         print("No members assigned.")
        
    #     cursor.close()
    #     db.close()

    def trainer_show_options(self,trainer_id):

        trainer=TrainerManagement()
        workout=WorkoutPlanManagement()
        while True:
            print("\n--- Trainer Dashboard ---")
            print("1. View Profile")
            print("2. Update Profile")
            print("3. View Assigned Members")
            print("4. Assign Workout Plan to a Member")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                trainer.view_trainer_by_id(trainer_id)
            elif choice == '2':
                name = input("Enter new name (or press Enter to skip): ") or None
                specialization = input("Enter new specialization (or press Enter to skip): ") or None
                contact_number = input("Enter new contact number (or press Enter to skip): ") or None
                trainer.update_trainer(trainer_id,name, specialization, contact_number)
            elif choice == '3':
                trainer.view_assigned_members(trainer_id)
            elif choice == '4':
                member_id = input("Enter Member ID: ")
                plan_id = input("Enter Workout Plan ID: ")
                workout.assign_workout_plan_to_member(member_id, plan_id)
            elif choice == '5':
                print("Exiting Trainer Dashboard...")
                break
            else:
                print("Invalid choice. Try again.")

def login():
    db = connect_to_db()
    cursor = db.cursor()
    
    while True:
        print("\n--- Login ---")
        print("1. Admin Login")
        print("2. Trainer Login")
        print("3. Member Login")
        print('\n---Register---')
        print('4. Member Register')
        print('5.Trainer Register')
        print('6.Exit...')
        choice = input("Enter your choice: ")
        
       
        
        if choice == '1':
            db = connect_to_db()
            cursor = db.cursor()
            username = input("Enter username: ")
            password = input("Enter password: ")
            cursor.execute("SELECT admin_id FROM admins WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()
            if user:
                print("Admin login successful!")
                a=Admin(user[0])
                a.admin_show_options()
                # Call admin dashboard function here
            else:
                print("Invalid admin credentials.")
        
        elif choice == '2':
            db = connect_to_db()
            cursor = db.cursor()
            username = input("Enter username: ")
            password = input("Enter password: ")
            cursor.execute("SELECT trainer_id FROM trainers WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()
            if user:
                print("Trainer login successful!")
                t=Trainer()
                t.trainer_show_options(user[0])
                
            else:
                print("Invalid trainer credentials.")
        
        elif choice == '3':
            db = connect_to_db()
            cursor = db.cursor()
            username = input("Enter username: ")
            password = input("Enter password: ")
            cursor.execute("SELECT member_id FROM members WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()

            if user:
                print("Member login successful!")
                m = Member(user[0])  # Extract the member_id from the tuple

                m.member_show_options()
                # Call member dashboard function here
            else:
                print("Invalid member credentials.")
        
        elif choice=='4':
            db = connect_to_db()
            cursor = db.cursor()
            print("\n---  New Member Details---")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            gender = input("Enter Gender (Male/Female/Other): ")
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            contact_number = int(input("Enter Contact Number: "))
            query = "INSERT INTO members (name, age, gender, username, password, contact_number) VALUES (%s, %s, %s, %s, %s, %s)"
            try:
                cursor.execute(query, (name, age, gender,
                            username, password, contact_number))
                db.commit()
                print("Member Registration successfully")
            except mysql.connector.IntegrityError:
                print("Error: Username already exists.")

        elif choice=='5':
            db = connect_to_db()
            cursor = db.cursor()
            name = input("Enter Name: ")
            specialization = input("Enter Specialization: ")
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            contact_number = input("Enter Contact Number: ")
            query = "INSERT INTO trainers (name, specialization, username, password, contact_number) VALUES (%s, %s, %s, %s, %s)"
            try:
                cursor.execute(query, (name, specialization,
                            username, password, contact_number))
                db.commit()
                print("Trainer Registration successfully!")
            except mysql.connector.IntegrityError:
                print("Error: Username already exists.")
        elif choice=='6':
            print('Exit...')
            break
        else:
            print("Invalid choice.")
        
        cursor.close()
        db.close()
        
login()