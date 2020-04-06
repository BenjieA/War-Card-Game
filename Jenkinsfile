pipeline{
        agent any
        stages{
                stage('Deploy Application'){
                        ssh """
                        ssh project@51.11.37.208 << EOF
                        rm -rf workspace
                        git clone http://github.com/BenjieA/workspace.git
                        cd workspace
                        export ${Version}=v1
                        docker stack deploy --compose-file docker-compose.yaml stack
                        """
                }
        }
}
