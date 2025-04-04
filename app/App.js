import { StatusBar } from 'expo-status-bar';
import { Pressable, StyleSheet, Text, TextInput, View } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>
     <View>
      <Image source={{uri:"https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Pok%C3%A9_Ball_icon.svg/2052px-Pok%C3%A9_Ball_icon.svg.png"}}/>
      widt={200}
      height={200}
     </View>
     <View>
       <Text style={styles.title}>Iniciar Sesion</Text>
       <Text style={styles.label}>Correo</Text>
       <TextInput style={styles.input}></TextInput>
       <Text style={styles.label}>Contraseña</Text>
       <TextInput style={styles.input}></TextInput>
       <Pressable style={styles.send.textButton}>Enviar</Pressable>
     </View>
     <View>{/*container-footer*/}
      <Text>Olvidaste Tu Contraseña</Text>
      <Text>Registrate</Text>
     </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    padding: 10,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title:{
    fontSize:30,
    fontWeight:"bold",
  },
  label:{
    fontSize:20,
    fontWeight:"Bold",
  },
  input:{
    borderRadius:10,
    borderWidth:2,
    borderColor:"black",
    fontSize:15,
    width:"auto",
  },
  send:{
    backgroundColor:"red",
    width:"auto",
    height:"auto",
    fontWeight:"bold",
    fontSize:20,
    borderRadius:10,
    marginTop:15,
    alignItems:"center",
    textButton:{
      color:"white",
      fontSize:20,
      fontWeight:"bold",
    }
  },
  containerFooter:{
    justifyContent:"center",
    text:{
      fontSize:20,
      margin:5
    }
    
  }


});
